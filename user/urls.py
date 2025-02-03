from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

# Use DRF's router to automatically generate URL conf for the viewset.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
