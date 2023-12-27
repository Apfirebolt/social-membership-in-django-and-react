from django.urls import path
from levels.views import ListPlotSellView, CreatePlotSellView, UpdatePlotSellView


urlpatterns = [
    path('', ListPlotSellView.as_view(), name='list'),
    path('create-sell', CreatePlotSellView.as_view(), name='create-sell'),
    path('<int:pk>', UpdatePlotSellView.as_view(), name='sell-update'),
]
