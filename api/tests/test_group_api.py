from django.test import TestCase
from core.models import UserGroups
from django.contrib.auth import get_user_model


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_group(**params):
    """Create and return a new group."""
    return UserGroups.objects.create(**params)


class UserGroupTestCase(TestCase):
    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )

    def test_create_user_group(self):
        """Test creating a user group."""
        group = create_group(
            name="Test Group",
            description="This is a test group",
            createdBy=self.user,
            createdAt="2022-01-01 00:00:00",
        )
        self.assertEqual(group.name, "Test Group")
        self.assertEqual(group.description, "This is a test group")
        self.assertEqual(group.createdBy, self.user)

    
