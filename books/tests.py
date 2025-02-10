from django.test import TestCase
from .models import Book

class BookModelTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            callNumber='123ABC',
            publisher='Test Publisher',
            isbn='1234567890',
            barcode='1234567890123',
            year_published='2023',
            shelfNumber='A1',
            description='A test book description.',
            language='English',
            subject='Test Subject',
            genre='Test Genre',
            value=100,
            method='Purchase',
            availability='Available',
            timesBorrowed=0,
            condition='Good'
        )

    def test_book_creation(self):
        """Test that a book can be created and its fields are correctly set"""
        self.assertEqual(self.book.title, 'Test Book')
        self.assertEqual(self.book.author, 'Test Author')
        self.assertEqual(self.book.callNumber, '123ABC')
        self.assertEqual(self.book.publisher, 'Test Publisher')
        self.assertEqual(self.book.isbn, '1234567890')
        self.assertEqual(self.book.barcode, '1234567890123')
        self.assertEqual(self.book.year_published, '2023')
        self.assertEqual(self.book.shelfNumber, 'A1')
        self.assertEqual(self.book.description, 'A test book description.')
        self.assertEqual(self.book.language, 'English')
        self.assertEqual(self.book.subject, 'Test Subject')
        self.assertEqual(self.book.genre, 'Test Genre')
        self.assertEqual(self.book.value, 100)
        self.assertEqual(self.book.method, 'Purchase')
        self.assertEqual(self.book.availability, 'Available')
        self.assertEqual(self.book.timesBorrowed, 0)
        self.assertEqual(self.book.condition, 'Good')

    def test_book_str(self):
        """Test the string representation of the book"""
        self.assertEqual(str(self.book), 'Test Book by Test Author')