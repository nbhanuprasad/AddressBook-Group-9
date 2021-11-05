from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

User = get_user_model()


class ProductTestCase(TestCase):

    def setUp(self): # Python's builtin unittest
        user_a = User(username='cfe', email='cfe@invalid.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = False

        user_a.save()
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'cfe3@invlalid.com', 'some_123_password')
        self.user_b = user_b

    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)
