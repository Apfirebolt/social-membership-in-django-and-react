from django.urls import path
from django.conf.urls.static import static
from social_membership import settings
from . views import LoginView, RegisterUser, UpdateAccountSettings, AccountDashboard
import django.contrib.auth.views as AuthViews


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', AuthViews.LogoutView.as_view(), name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('profile', UpdateAccountSettings.as_view(), name='profile'),
    path('dashboard', AccountDashboard.as_view(), name='dashboard'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)