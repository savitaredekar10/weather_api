from django.urls import path
from .views import get_historical_weather

urlpatterns = [
    path('historical-weather/', get_historical_weather, name='get_historical_weather'),
]
