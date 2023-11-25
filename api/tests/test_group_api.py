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

def detail_url(group_id):
    """Create and return a group detail URL."""
    return reverse('api:detail-groups', args=[group_id])


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
            'createdAt': '2022-01-01 00:00:00',
        }
        res = self.client.post(CREATE_GROUP_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED, "Expected status code 201, but got {}".format(res.status_code))
        group = UserGroups.objects.get(name=payload['name'])
        self.assertEqual(group.name, payload['name'])
        self.assertEqual(group.description, payload['description'])

    
    def test_create_group_invalid(self):
        """Test creating a group with invalid payload."""
        payload = {
            'name': '',
            'description': '',
            'createdAt': '2022-01-01 00:00:00',
        }
        res = self.client.post(CREATE_GROUP_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST, "Expected status code 400, but got {}".format(res.status_code))
        group = UserGroups.objects.filter(name=payload['name'])
        self.assertEqual(len(group), 0)

    
    def test_list_group(self):
        """Test listing groups."""
        payload = {
            'name': 'Test Group',
            'description': 'This is a test group',
            'createdAt': '2022-01-01 00:00:00',
        }
        self.client.post(CREATE_GROUP_URL, payload)
        res = self.client.get(LIST_GROUP_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK, "Expected status code 200, but got {}".format(res.status_code))
        group = UserGroups.objects.get(name=payload['name'])
        self.assertEqual(group.name, payload['name'])

    
    def test_single_group(self):
        """Test viewing a group."""
        payload = {
            'name': 'Test Group',
            'description': 'This is a test group',
            'createdAt': '2022-01-01 00:00:00',
            'createdBy': self.user,
        }
        group = create_group(**payload)
        res = self.client.get(detail_url(group.id))
        self.assertEqual(res.status_code, status.HTTP_200_OK, "Expected status code 200, but got {}".format(res.status_code))
        self.assertEqual(res.data['name'], group.name)
        self.assertEqual(res.data['description'], group.description)

    
    def test_update_group(self):
        """Test updating a group."""
        payload = {
            'name': 'Test Group',
            'description': 'This is a test group',
            'createdAt': '2022-01-01 00:00:00',
            'createdBy': self.user,
        }
        group = create_group(**payload)
        payload = {
            'name': 'Test Group Updated',
            'description': 'This is a test group updated',
            'createdAt': '2022-01-01 00:00:00',
            'createdBy': self.user,
        }
        res = self.client.put(detail_url(group.id), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK, "Expected status code 200, but got {}".format(res.status_code))
        group.refresh_from_db()
        self.assertEqual(group.name, payload['name'])
        self.assertEqual(group.description, payload['description'])

    
    def test_delete_group(self):
        """Test deleting a group."""
        payload = {
            'name': 'Test Group',
            'description': 'This is a test group',
            'createdAt': '2022-01-01 00:00:00',
            'createdBy': self.user,
        }
        group = create_group(**payload)
        res = self.client.delete(detail_url(group.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT, "Expected status code 204, but got {}".format(res.status_code))
        group = UserGroups.objects.filter(name=payload['name'])
        self.assertEqual(len(group), 0)

    
