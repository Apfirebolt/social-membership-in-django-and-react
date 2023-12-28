from django.urls import path
from core.views import ListPlotView, UpdatePlotView, CreatePlotView, CreatePlotImageView, ListPlotImageView


urlpatterns = [
    path('', ListPlotView.as_view(), name='plot-list'),
    path('create-plot', CreatePlotView.as_view(), name='create-plot'),
    path('<int:pk>', UpdatePlotView.as_view(), name='plot-update'),
    path('create-plot-image', CreatePlotImageView.as_view(), name='create-plot-image'),
    path('plot-images', ListPlotImageView.as_view(), name='plot-images'),
]
