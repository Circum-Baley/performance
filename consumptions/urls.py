from django.urls import path, include

from consumptions.models import Consumption
from consumptions.views import ConsumptionCreateView, ConsumptionListView, ConsumptionsDetailView, \
    ConsumptionDeleteView, ConsumptionUpdateView

# urlspatterns = [
#     path('', HomePageView.as_view(), name="base"),
# ]

consumptions_patterns = ([
                             # path('', HomePageView.as_view(), name="home"),
                             path('', ConsumptionListView.as_view(), name='consumptions'),
                             path('<int:pk>/<slug:slug>/', ConsumptionsDetailView.as_view(), name='consumption'),
                             path('create/', ConsumptionCreateView.as_view(), name="create"),
                             path('update/<int:pk>/', ConsumptionUpdateView.as_view(), name="update"),
                             path('delete/<int:pk>/', ConsumptionDeleteView.as_view(), name="delete"),
                         ], 'consumptions')
