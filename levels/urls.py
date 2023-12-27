from django.urls import path
from django.conf.urls.static import static
from social_membership import settings
from . views import ListLevelView, DetailLevelView, CreateLevelView


urlpatterns = [
    path('', ListLevelView.as_view(), name='list'),
    path('create-level', CreateLevelView.as_view(), name='create-level'),
    path('levels/<int:pk>', DetailLevelView.as_view(), name='level-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)