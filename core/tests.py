from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages import get_messages
from django.core.exceptions import ValidationError
from PIL import Image
import tempfile
import os

from .models import UserGroups, Message, GroupMembers, Plot, PlotImages
from .forms import GroupForm, PlotForm, PlotImageForm

User = get_user_model()


class UserGroupsModelTest(TestCase):
    """Test cases for UserGroups model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        
    def test_create_user_group(self):
        """Test creating a user group"""
        group = UserGroups.objects.create(
            name='Test Group',
            description='Test Description',
            createdBy=self.user
        )
        self.assertEqual(group.name, 'Test Group')
        self.assertEqual(group.description, 'Test Description')
        self.assertEqual(group.createdBy, self.user)
        self.assertTrue(group.createdAt)
        
    def test_user_group_str_method(self):
        """Test string representation of UserGroups"""
        group = UserGroups.objects.create(
            name='Test Group',
            createdBy=self.user
        )
        self.assertEqual(str(group), 'Test Group')
        
    def test_user_group_verbose_name_plural(self):
        """Test verbose name plural"""
        self.assertEqual(UserGroups._meta.verbose_name_plural, 'User Group')


class MessageModelTest(TestCase):
    """Test cases for Message model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        self.group = UserGroups.objects.create(
            name='Test Group',
            createdBy=self.user
        )
        
    def test_create_message(self):
        """Test creating a message"""
        message = Message.objects.create(
            text='Test message',
            sender=self.user,
            group=self.group
        )
        self.assertEqual(message.text, 'Test message')
        self.assertEqual(message.sender, self.user)
        self.assertEqual(message.group, self.group)
        self.assertTrue(message.createdAt)
        
    def test_message_str_method(self):
        """Test string representation of Message"""
        message = Message.objects.create(
            text='Test message',
            sender=self.user,
            group=self.group
        )
        self.assertEqual(str(message), 'Test message')


class GroupMembersModelTest(TestCase):
    """Test cases for GroupMembers model"""
    
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='user1@example.com',
            password='testpass123',
            username='user1'
        )
        self.user2 = User.objects.create_user(
            email='user2@example.com',
            password='testpass123',
            username='user2'
        )
        self.group = UserGroups.objects.create(
            name='Test Group',
            createdBy=self.user1
        )
        
    def test_create_group_member(self):
        """Test creating a group member"""
        member = GroupMembers.objects.create(
            group=self.group,
            member=self.user2,
            level='premium'
        )
        self.assertEqual(member.group, self.group)
        self.assertEqual(member.member, self.user2)
        self.assertEqual(member.level, 'premium')
        self.assertTrue(member.createdAt)
        
    def test_group_member_str_method(self):
        """Test string representation of GroupMembers"""
        member = GroupMembers.objects.create(
            group=self.group,
            member=self.user2
        )
        expected_str = f"{self.group.name} - {self.user2.username}"
        self.assertEqual(str(member), expected_str)


class PlotModelTest(TestCase):
    """Test cases for Plot model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        
    def test_create_plot(self):
        """Test creating a plot"""
        plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            description='Test plot description',
            createdBy=self.user
        )
        self.assertEqual(plot.location, 'Test Location')
        self.assertEqual(plot.price, 100000)
        self.assertEqual(plot.description, 'Test plot description')
        self.assertEqual(plot.createdBy, self.user)
        self.assertTrue(plot.createdAt)
        
    def test_plot_str_method(self):
        """Test string representation of Plot"""
        plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            createdBy=self.user
        )
        expected_str = f"{plot.location} - {plot.price}"
        self.assertEqual(str(plot), expected_str)


class PlotImagesModelTest(TestCase):
    """Test cases for PlotImages model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        self.plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            createdBy=self.user
        )
        
    def create_test_image(self):
        """Helper method to create a test image"""
        image = Image.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        image.save(temp_file, format='JPEG')
        temp_file.seek(0)
        return SimpleUploadedFile(
            name='test.jpg',
            content=temp_file.read(),
            content_type='image/jpeg'
        )
        
    def test_create_plot_image(self):
        """Test creating a plot image"""
        test_image = self.create_test_image()
        plot_image = PlotImages.objects.create(
            plot=self.plot,
            image=test_image,
            title='Test Image'
        )
        self.assertEqual(plot_image.plot, self.plot)
        self.assertEqual(plot_image.title, 'Test Image')
        self.assertTrue(plot_image.createdAt)
        self.assertTrue(plot_image.image)
        
    def test_plot_image_str_method(self):
        """Test string representation of PlotImages"""
        test_image = self.create_test_image()
        plot_image = PlotImages.objects.create(
            plot=self.plot,
            image=test_image,
            title='Test Image'
        )
        expected_str = f"{self.plot.location} - {plot_image.title}"
        self.assertEqual(str(plot_image), expected_str)


class GroupFormTest(TestCase):
    """Test cases for GroupForm"""
    
    def test_valid_group_form(self):
        """Test valid group form"""
        form_data = {
            'name': 'Test Group',
            'description': 'Test description for the group'
        }
        form = GroupForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_group_form_short_name(self):
        """Test invalid group form with short name"""
        form_data = {
            'name': 'Abc',  # Less than 4 characters
            'description': 'Test description'
        }
        form = GroupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Name cannot be shorter than 4 letters.', 
                     form.errors.get('name', []))
        
    def test_group_form_required_fields(self):
        """Test group form with missing required fields"""
        form = GroupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)


class PlotFormTest(TestCase):
    """Test cases for PlotForm"""
    
    def test_valid_plot_form(self):
        """Test valid plot form"""
        form_data = {
            'location': 'Test Location',
            'price': '100000',
            'description': 'Test plot description'
        }
        form = PlotForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_plot_form_required_fields(self):
        """Test plot form with missing required fields"""
        form = PlotForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('location', form.errors)
        self.assertIn('price', form.errors)


class PlotImageFormTest(TestCase):
    """Test cases for PlotImageForm"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        self.plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            createdBy=self.user
        )
        
    def create_test_image(self):
        """Helper method to create a test image"""
        image = Image.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        image.save(temp_file, format='JPEG')
        temp_file.seek(0)
        return SimpleUploadedFile(
            name='test.jpg',
            content=temp_file.read(),
            content_type='image/jpeg'
        )
        
    def test_valid_plot_image_form(self):
        """Test valid plot image form"""
        test_image = self.create_test_image()
        form_data = {
            'plot': self.plot.id,
            'title': 'Test Image Title'
        }
        form = PlotImageForm(data=form_data, files={'image': test_image})
        self.assertTrue(form.is_valid())


class PlotViewsTest(TestCase):
    """Test cases for Plot views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        self.plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            description='Test description',
            createdBy=self.user
        )
        
    def test_list_plot_view_requires_login(self):
        """Test that list plot view requires login"""
        response = self.client.get('/plots/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
        
    def test_list_plot_view_authenticated(self):
        """Test list plot view with authenticated user"""
        self.client.login(email='testuser@example.com', password='testpass123')
        response = self.client.get('/plots/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Location')
        
    def test_detail_plot_view_authenticated(self):
        """Test detail plot view with authenticated user"""
        self.client.login(email='testuser@example.com', password='testpass123')
        response = self.client.get(f'/plots/detail/{self.plot.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Location')
        
    def test_create_plot_view_get(self):
        """Test GET request to create plot view"""
        self.client.login(email='testuser@example.com', password='testpass123')
        response = self.client.get('/plots/create-plot')
        self.assertEqual(response.status_code, 200)
        
    def test_create_plot_view_post_valid(self):
        """Test POST request to create plot view with valid data"""
        self.client.login(email='testuser@example.com', password='testpass123')
        form_data = {
            'location': 'New Test Location',
            'price': '150000',
            'description': 'New test description'
        }
        response = self.client.post('/plots/create-plot', data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        
        # Check if plot was created
        new_plot = Plot.objects.filter(location='New Test Location').first()
        self.assertIsNotNone(new_plot)
        self.assertEqual(new_plot.createdBy, self.user)
        
    def test_update_plot_view_get(self):
        """Test GET request to update plot view"""
        self.client.login(email='testuser@example.com', password='testpass123')
        response = self.client.get(f'/plots/{self.plot.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Location')
        
    def test_update_plot_view_post_valid(self):
        """Test POST request to update plot view with valid data"""
        self.client.login(email='testuser@example.com', password='testpass123')
        form_data = {
            'location': 'Updated Location',
            'price': '200000',
            'description': 'Updated description'
        }
        response = self.client.post(f'/plots/{self.plot.id}', data=form_data)
        self.assertEqual(response.status_code, 302)
        
        # Check if plot was updated
        updated_plot = Plot.objects.get(id=self.plot.id)
        self.assertEqual(updated_plot.location, 'Updated Location')
        self.assertEqual(updated_plot.price, 200000)


class PlotImageViewsTest(TestCase):
    """Test cases for PlotImage views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpass123',
            username='testuser'
        )
        self.plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            createdBy=self.user
        )
        
    def create_test_image(self):
        """Helper method to create a test image"""
        image = Image.new('RGB', (100, 100), color='red')
        temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        image.save(temp_file, format='JPEG')
        temp_file.seek(0)
        return SimpleUploadedFile(
            name='test.jpg',
            content=temp_file.read(),
            content_type='image/jpeg'
        )
        
    def test_list_plot_image_view_requires_login(self):
        """Test that list plot image view requires login"""
        response = self.client.get('/plots/plot-images')
        self.assertEqual(response.status_code, 302)  # Redirect to login
        
    def test_list_plot_image_view_authenticated(self):
        """Test list plot image view with authenticated user"""
        self.client.login(email='testuser@example.com', password='testpass123')
        response = self.client.get('/plots/plot-images')
        self.assertEqual(response.status_code, 200)
        
    def test_create_plot_image_view_get(self):
        """Test GET request to create plot image view"""
        self.client.login(email='testuser@example.com', password='testpass123')
        response = self.client.get('/plots/create-plot-image')
        self.assertEqual(response.status_code, 200)


class ModelRelationshipsTest(TestCase):
    """Test model relationships and related queries"""
    
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='user1@example.com',
            password='testpass123',
            username='user1'
        )
        self.user2 = User.objects.create_user(
            email='user2@example.com',
            password='testpass123',
            username='user2'
        )
        
    def test_user_group_relationships(self):
        """Test relationships between users and groups"""
        group = UserGroups.objects.create(
            name='Test Group',
            description='Test Description',
            createdBy=self.user1
        )
        
        # Add members to group
        member1 = GroupMembers.objects.create(
            group=group,
            member=self.user1,
            level='admin'
        )
        member2 = GroupMembers.objects.create(
            group=group,
            member=self.user2,
            level='member'
        )
        
        # Test related queries
        self.assertEqual(group.group_members.count(), 2)
        self.assertEqual(group.createdBy, self.user1)
        
        # Test reverse relationships
        user1_created_groups = self.user1.group_created_by.all()
        self.assertEqual(user1_created_groups.count(), 1)
        self.assertEqual(user1_created_groups.first(), group)
        
    def test_message_relationships(self):
        """Test message relationships"""
        group = UserGroups.objects.create(
            name='Test Group',
            createdBy=self.user1
        )
        
        message = Message.objects.create(
            text='Test message',
            sender=self.user1,
            group=group
        )
        
        # Test relationships
        self.assertEqual(message.sender, self.user1)
        self.assertEqual(message.group, group)
        self.assertEqual(group.user_groups.count(), 1)
        
    def test_plot_relationships(self):
        """Test plot and plot images relationships"""
        plot = Plot.objects.create(
            location='Test Location',
            price=100000,
            createdBy=self.user1
        )
        
        # Create test image
        test_image = SimpleUploadedFile(
            name='test.jpg',
            content=b'fake image content',
            content_type='image/jpeg'
        )
        
        plot_image = PlotImages.objects.create(
            plot=plot,
            image=test_image,
            title='Test Image'
        )
        
        # Test relationships
        self.assertEqual(plot_image.plot, plot)
        self.assertEqual(plot.plot_images.count(), 1)
        self.assertEqual(plot.createdBy, self.user1)


