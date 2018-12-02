# Generated by Django 2.1.3 on 2018-12-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20181124_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='airdata',
            name='humidity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airdata',
            name='temperature',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airdata',
            name='tgs2602',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
