# Generated by Django 3.2.4 on 2021-08-15 19:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0020_auto_20210815_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 15, 19, 57, 23, 617232, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.datetime(2021, 8, 15, 19, 57, 23, 604161, tzinfo=utc)),
        ),
    ]