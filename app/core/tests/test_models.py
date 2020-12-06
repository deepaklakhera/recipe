from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@1234.com',password='test@1234'):

    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creatin an new user with email"""
        email="django@123.com"
        password="Test@123"
        user=get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_mormalize_email(self):
        email="django@HerOku.COM"
        password="Test@123"
        user=get_user_model().objects.create_user(email=email,password=password)
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_user(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
    
    def test_create_new_superuser(self):

        user=get_user_model().objects.create_superuser('test@123.com','test.123')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        tag=models.Tag.objects.create(
            user=sample_user(),name='Vegan'
        )
        self.assertEqual(str(tag),tag.name)
        