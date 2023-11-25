from django.urls import path
from . views import ListCustomUsersApiView, CreateCustomUserApiView, DetailCustomUserApiView, ListUserGroupsApiView, \
    CreateUserGroupsApiView, ListMessagesApiView, CreateMessageApiView, DetailUserGroupsApiView, DetailMessageApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', CreateCustomUserApiView.as_view(), name='signup'),
    path('login', TokenObtainPairView.as_view(), name='signin'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('profile', DetailCustomUserApiView.as_view(), name='me'),
    path('users', ListCustomUsersApiView.as_view(), name='list-users'),
    path('groups', ListUserGroupsApiView.as_view(), name='list-groups'),
    path('groups/<int:pk>', DetailUserGroupsApiView.as_view(), name='detail-groups'),
    path('create-group', CreateUserGroupsApiView.as_view(), name='create-group'),
    path('messages', ListMessagesApiView.as_view(), name='list-messages'),
    path('messages/<int:pk>', DetailMessageApiView.as_view(), name='detail-messages'),
    path('create-message', CreateMessageApiView.as_view(), name='create-message'),
    
]