from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import User, Student, Staff
from .serializers import UserSerializer, StudentSerializer, StaffSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for the User model:
    list, create, retrieve, update, and destroy.
    """
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Optionally, you can override methods to customize behavior.
    # For example, you might restrict deletion or add filtering here.

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides standard actions for the Student model:
    list, create, retrieve, update, and destroy.
    """
    queryset = Student.objects.all().order_by('-created_at')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class StaffViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides standard CRUD actions (list, create, retrieve, update, destroy)
    for the Staff model.
    """
    queryset = Staff.objects.all().order_by('-created_at')
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]