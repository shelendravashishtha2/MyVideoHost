# Generated by Django 3.0.3 on 2020-08-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csed', '0004_auto_20200818_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='pub_date',
            field=models.DateTimeField(verbose_name='publish_date'),
        ),
    ]