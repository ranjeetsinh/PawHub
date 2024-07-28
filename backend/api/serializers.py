from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Stray

class UserSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = User
        geo_field = "location"
        fields = ('id', 'email', 'name', 'dob', 'phone_number', 'profile_photo', 'location', 'state', 'city', 'pincode', 'profession', 'date_joined')
         

class StraySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Stray
        geo_field = "location"
        fields = ('id', 'species', 'name', 'age', 'description', 'location', 'photo', 'reported_by', 'is_adopted', 'date_reported')