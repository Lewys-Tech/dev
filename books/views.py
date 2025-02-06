from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing book instances.
    """
    queryset = Book.objects.all().order_by('-dateAdded')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
