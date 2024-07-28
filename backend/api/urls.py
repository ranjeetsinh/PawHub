# api/urls.py

from django.urls import path
from .views import UserDetailView, StrayListCreateView, StrayDetailView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('strays/', StrayListCreateView.as_view(), name='stray-list-create'),
    path('strays/<int:pk>/', StrayDetailView.as_view(), name='stray-detail'),
]
