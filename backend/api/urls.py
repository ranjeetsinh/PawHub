# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserDetailView, StrayViewSet

router = DefaultRouter()
router.register(r'strays', StrayViewSet)

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),
]
