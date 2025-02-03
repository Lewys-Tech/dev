from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import User
from .serializers import UserSerializer

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
