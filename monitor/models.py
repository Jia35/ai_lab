from django.db import models
from django.utils import timezone


class AirData(models.Model):
    pm01 = models.DecimalField(max_digits=4, decimal_places=0)
    pm25 = models.DecimalField(max_digits=4, decimal_places=0)
    pm10 = models.DecimalField(max_digits=4, decimal_places=0)
    creation_date = models.DateTimeField(default=timezone.now)
