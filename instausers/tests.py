from django.test import TestCase
from .models import UserAccount


# Create your tests here.

class ProfileTest(TestCase):

    def test_useraccount_model_has_profile(self):
        user = UserAccount(
            email="andrewjohn@gmail.com",
            username="andyjohn",
            password="andy123"
        )
        user.save()

        self.assertTrue(
            hasattr(user, 'profile')
        )
