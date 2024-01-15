from django.db import models
from user_accounts.models import CustomUser 
from django.utils import timezone
from datetime import datetime


class WeatherData(models.Model):
    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location    = models.CharField(max_length=255)
    latitude    = models.FloatField()
    longitude   = models.FloatField()
    temperature = models.FloatField()
    precipitation = models.FloatField()
    cloud_cover = models.FloatField()
    timestamp   = models.DateTimeField()

    def save(self, *args, **kwargs):
         # Convert timestamp to datetime if it's a string
        if isinstance(self.timestamp, str):
            self.timestamp = datetime.strptime(self.timestamp, '%Y-%m-%dT%H:%M')

        # Ensure timestamp is an aware datetime before saving
        if self.timestamp and timezone.is_naive(self.timestamp):
            self.timestamp = timezone.make_aware(self.timestamp)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.location} - {self.timestamp}"
