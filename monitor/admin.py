from django.contrib import admin
from .models import AirData


@admin.register(AirData)
class AirDataAdmin(admin.ModelAdmin):
    list_display = ('pm1', 'pm25', 'pm10', 'mq9', 'mq135', 'creation_date')
    ordering = ('creation_date',)
