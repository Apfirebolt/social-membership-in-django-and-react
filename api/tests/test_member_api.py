from django.test import TestCase
from core.models import UserGroups, GroupMembers
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


CREATE_GROUP_MEMBERS_URL = reverse('api:create-group-members')


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_group(**params):
    """Create and return a new group."""
    return UserGroups.objects.create(**params)


def delete_url(membership_id):
    """Delete a group member relationship."""
    return reverse('api:delete-group-members', args=[membership_id])


class GroupMemberTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(
            email="test@gmail.com",
            username="Test User",
            password="test123",
        )
        self.client.force_authenticate(user=self.user)


    def test_create_member_api(self):
        """Test creating a group member."""
        group = create_group(
            name='Test Group',
            description='This is a test group',
            createdBy=self.user,
        )
        payload = {
            'group': group.id,
            'member': self.user.id,
        }
        res = self.client.post(CREATE_GROUP_MEMBERS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED, "Expected status code 201, but got {}".format(res.status_code))
        member = GroupMembers.objects.get(member=self.user)
        self.assertEqual(member.member.id, payload['member'])
        self.assertEqual(member.group.id, payload['group'])

    
    def test_delete_member_api(self):
        """Test deleting a group member."""
        group = create_group(
            name='Test Group',
            description='This is a test group',
            createdBy=self.user,
        )
        member = GroupMembers.objects.create(
            group=group,
            member=self.user,
        )
        res = self.client.delete(delete_url(member.id))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT, "Expected status code 204, but got {}".format(res.status_code))
        member = GroupMembers.objects.filter(member=self.user)
        self.assertEqual(len(member), 0)
    
