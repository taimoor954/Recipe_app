"""
Test for moodel
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTest(TestCase):
    """Test model"""

    def test_create_user_with_email_successful(self):
        email = 'test@example.com'
        password="testpass123"


        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email is normalized for users"""

        sample_emails = [
            ['test1@EXAMPLE.COM','test1@example.com'],
            ['Test2@Example.com' , 'Test2@example.com'],
            ['TEST3@example.COM' , 'TEST3@example.com']
        ]

        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email , 'sample123')
            self.assertEqual(user.email , expected)

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')