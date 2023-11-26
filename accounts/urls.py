from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from social_membership import settings
from . views import home_view, LoginView, RegisterUser, UpdateAccountSettings
import django.contrib.auth.views as AuthViews


urlpatterns = [
    path('', home_view, name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', AuthViews.LogoutView.as_view(), name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('settings', UpdateAccountSettings.as_view(), name='settings'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)