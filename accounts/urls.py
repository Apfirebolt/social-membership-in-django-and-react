from django.urls import path
from django.conf.urls.static import static
from social_membership import settings
from . views import LoginView, RegisterUser, UpdateAccountSettings, AccountDashboard, UserGroupDetailView, CreateGroup, Membership
import django.contrib.auth.views as AuthViews


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', AuthViews.LogoutView.as_view(), name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile', UpdateAccountSettings.as_view(), name='profile'),
    path('dashboard', AccountDashboard.as_view(), name='dashboard'),
    path('group/<int:pk>', UserGroupDetailView.as_view(), name='group-detail'),
    path('create-group', CreateGroup.as_view(), name='create-group'),
    path('membership', Membership.as_view(), name='membership'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)