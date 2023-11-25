from django.test import TestCase
from core.models import UserGroups, Message
from django.contrib.auth import get_user_model


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_group(**params):
    """Create and return a new group."""
    return UserGroups.objects.create(**params)

def create_message(**params):
    """Create and return a new message."""
    return Message.objects.create(**params)


class MessageTestCase(TestCase):
    def setUp(self):
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )

        self.group = create_group(
            name="Test Group",
            description="This is a test group",
            createdBy=self.user,
            createdAt="2022-01-01 00:00:00",
        )

    def test_create_message(self):
        """Test creating a message."""
        message = create_message(
            text="This is a test message",
            sender=self.user,
            createdAt="2022-01-01 00:00:00",
            group=self.group,
        )
        self.assertEqual(message.text, "This is a test message")
        self.assertEqual(message.sender, self.user)
        self.assertEqual(message.group, self.group)

    
    def test_get_messages(self):
        """Test getting messages."""
        message1 = create_message(
            text="This is a test message",
            sender=self.user,
            createdAt="2022-01-01 00:00:00",
            group=self.group,
        )
        message2 = create_message(
            text="This is a test message 2",
            sender=self.user,
            createdAt="2022-01-01 00:00:00",
            group=self.group,
        )
        response = self.client.get('/api/messages/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['text'], "This is a test message")
        self.assertEqual(response.data[0]['sender'], self.user.id)
        self.assertEqual(response.data[0]['group'], self.group.id)

    
