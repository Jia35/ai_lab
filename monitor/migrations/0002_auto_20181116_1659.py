# Generated by Django 2.1.3 on 2018-11-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airdata',
            name='pm01',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='airdata',
            name='pm10',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='airdata',
            name='pm25',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
    ]
