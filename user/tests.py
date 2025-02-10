from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def test_create_user(self):
        """Test creating a new user"""
        email = 'test@example.com'
        first_name = 'John'
        second_name = 'Doe'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            first_name=first_name,
            second_name=second_name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.second_name, second_name)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """Test creating a new superuser"""
        email = 'super@example.com'
        first_name = 'Super'
        second_name = 'User'
        password = 'superpass123'
        user = get_user_model().objects.create_superuser(
            email=email,
            first_name=first_name,
            second_name=second_name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.second_name, second_name)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)