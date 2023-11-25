from django.test import TestCase
from core.models import UserGroups
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_GROUP_URL = reverse('api:create-group')
LIST_GROUP_URL = reverse('api:list-groups')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_group(**params):
    """Create and return a new group."""
    return UserGroups.objects.create(**params)


class UserGroupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )
        self.client.force_authenticate(user=self.user)

    def test_create_group(self):
        """Test creating a group."""
        payload = {
            'name': 'Test Group',
            'description': 'This is a test group',
            'createdBy': self.user.id,  # Pass the primary key instead of the user object
            'createdAt': '2022-01-01 00:00:00',
        }
        res = self.client.post(CREATE_GROUP_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED, "Expected status code 201, but got {}".format(res.status_code))
        group = UserGroups.objects.get(name=payload['name'])
        self.assertEqual(group.name, payload['name'])
        self.assertEqual(group.description, payload['description'])

    
    def test_get_groups(self):
        """Test getting groups."""
        group1 = create_group(
            name="Test Group",
            description="This is a test group",
            createdBy=self.user,
            createdAt="2022-01-01 00:00:00",
        )
        group2 = create_group(
            name="Test Group 2",
            description="This is a test group 2",
            createdBy=self.user,
            createdAt="2022-01-01 00:00:00",
        )
        res = self.client.get(LIST_GROUP_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK, "Expected status code 200, but got {}".format(res.status_code))




    

    
