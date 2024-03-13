from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email= "test@example.com"
        password = "testpass"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        sample_emails= [
            ['test@EXAMPLE.com', 'test@example.com'],
            ['Test2@EXAMPLE.com', 'Test2@example.com'],
            ['tesT3@EXAMPLE.com', 'tesT3@example.com'],
            ['TEST4@EXAMPLE.com', 'TEST4@example.com'],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'pass')
            self.assertEqual(user.email, expected)

    def test_new_user_without_eamil_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'pass')

    def test_create_superuser(self):
        user=get_user_model().objects.create_superuser(
            'test@example.com',
            'pass'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


