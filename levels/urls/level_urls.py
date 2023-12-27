from django.urls import path
from levels.views import ListLevelView, UpdateLevelView, CreateLevelView


urlpatterns = [
    path('', ListLevelView.as_view(), name='list'),
    path('create-level', CreateLevelView.as_view(), name='create-level'),
    path('<int:pk>', UpdateLevelView.as_view(), name='level-update'),
]
