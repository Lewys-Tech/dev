from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import User, Student, Staff, OtherUser
from .serializers import UserSerializer, StudentSerializer, StaffSerializer, OtherUserSerializer

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

    def perform_create(self, serializer):
        # Automatically assign the current logged-in user to the student
        serializer.save(user=self.request.user)


class StaffViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides standard CRUD actions (list, create, retrieve, update, destroy)
    for the Staff model.
    """
    queryset = Staff.objects.all().order_by('-created_at')
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OtherUserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides standard CRUD actions for OtherUser.
    """
    queryset = OtherUser.objects.all().order_by('-user__user_id')
    serializer_class = OtherUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        