# Generated by Django 3.0.3 on 2020-08-18 23:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('csed', '0008_auto_20200819_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 18, 23, 52, 7, 64141, tzinfo=utc)),
        ),
    ]