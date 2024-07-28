from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, StraySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Stray

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user
    

class StrayListCreateView(generics.ListCreateAPIView):
    queryset = Stray.objects.all()
    serializer_class = StraySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)

class StrayDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stray.objects.all()
    serializer_class = StraySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]