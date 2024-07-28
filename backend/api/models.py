from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import Group, Permission

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, name, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    location = geomodels.PointField(null=True, blank=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

     # Added related_name attributes
    groups = models.ManyToManyField(Group, related_name='api_users')
    user_permissions = models.ManyToManyField(Permission, related_name='api_users')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class Stray(models.Model):
    SPECIES_CHOICES = [
        ('puppy', 'Puppy'),
        ('kitten', 'Kitten'),
    ]

    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    location = geomodels.PointField()
    photo = models.ImageField(upload_to='stray_photos/', blank=True, null=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_adopted = models.BooleanField(default=False)
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"