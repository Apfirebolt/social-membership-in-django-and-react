from django.test import TestCase
from core.models import UserGroups, Message
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from core.models import Message


CREATE_GROUP_URL = reverse('api:create-group')
CREATE_MESSAGE_URL = reverse('api:create-message')
LIST_MESSAGE_URL = reverse('api:list-messages')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_group(**params):
    """Create and return a new group."""
    return UserGroups.objects.create(**params)

def detail_url(message_id):
    """Create and return a message detail URL."""
    return reverse('api:detail-messages', args=[message_id])


class UserGroupTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )
        self.client.force_authenticate(user=self.user)

    
    def test_create_message(self):
        """Test creating a message."""
        group = create_group(
            name='Test Group',
            description='This is a test group',
            createdAt='2022-01-01 00:00:00',
            createdBy=self.user
        )
        payload = {
            'text': 'Test Message',
            'group': group.id,
            'createdAt': '2022-01-01 00:00:00',
        }
        res = self.client.post(CREATE_MESSAGE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED, "Expected status code 201, but got {}".format(res.status_code))
        message = Message.objects.get(text=payload['text'])
        self.assertEqual(message.text, payload['text'])

    
    def test_create_message_invalid(self):
        """Test creating a message with invalid payload."""
        payload = {
            'text': '',
            'group': '',
            'createdAt': '2022-01-01 00:00:00',
        }
        res = self.client.post(CREATE_MESSAGE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST, "Expected status code 400, but got {}".format(res.status_code))

    
    def test_update_message(self):
        """Test updating a message."""
        group = create_group(
            name='Test Group',
            description='This is a test group',
            createdAt='2022-01-01 00:00:00',
            createdBy=self.user
        )
        message = Message.objects.create(
            text='Test Message',
            group=group,
            createdAt='2022-01-01 00:00:00',
            sender=self.user
        )
        payload = {
            'text': 'Test Message Updated',
            'group': group.id,
            'createdAt': '2022-01-01 00:00:00',
        }
        url = detail_url(message.id)
        res = self.client.put(url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK, "Expected status code 200, but got {}".format(res.status_code))
        message.refresh_from_db()
        self.assertEqual(message.text, payload['text'])

    
    def test_delete_message(self):
        """Test deleting a message."""
        group = create_group(
            name='Test Group',
            description='This is a test group',
            createdAt='2022-01-01 00:00:00',
            createdBy=self.user
        )
        message = Message.objects.create(
            text='Test Message',
            group=group,
            createdAt='2022-01-01 00:00:00',
            sender=self.user
        )
        url = detail_url(message.id)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT, "Expected status code 204, but got {}".format(res.status_code))
        message_exists = Message.objects.filter(id=message.id).exists()
        self.assertFalse(message_exists)
