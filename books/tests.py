from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Book

User = get_user_model()

class BookAPITestCase(APITestCase):

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="securepassword"
        )
        self.client.force_authenticate(user=self.user)

        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            callNumber="123ABC",
            publisher="Test Publisher",
            isbn="978-3-16-148410-0",
            availability="Available"
        )

    def test_get_books_list(self):
        """Test retrieving books list"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """Test creating a book"""
        data = {
            "title": "New Book",
            "author": "Jane Doe",
            "callNumber": "456DEF",
            "publisher": "Another Publisher",
            "isbn": "978-1-23-456789-7",
            "availability": "Available"
        }
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating a book"""
        data = {"title": "Updated Title"}
        response = self.client.patch(f"/api/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

