from django.db import models
from django.utils import timezone


class AirData(models.Model):
    pm1 = models.DecimalField(max_digits=4, decimal_places=0)
    pm25 = models.DecimalField(max_digits=4, decimal_places=0)
    pm10 = models.DecimalField(max_digits=4, decimal_places=0)
    mq9 = models.DecimalField(max_digits=4, decimal_places=0)
    mq135 = models.DecimalField(max_digits=4, decimal_places=0)
    creation_date = models.DateTimeField(default=timezone.now)
