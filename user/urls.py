from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StudentViewSet, StaffViewSet, OtherUserViewSet

# Use DRF's router to automatically generate URL conf for the viewset.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'other-users', OtherUserViewSet, basename='other-user')


urlpatterns = [
    path('', include(router.urls)),
]
