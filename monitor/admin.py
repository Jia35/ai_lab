from django.contrib import admin
from .models import AirData


@admin.register(AirData)
class AirDataAdmin(admin.ModelAdmin):
    list_display = ('pm01', 'pm25', 'pm10', 'creation_date')
    list_filter = ('pm01', 'pm25', 'pm10')
    ordering = ('creation_date',)
