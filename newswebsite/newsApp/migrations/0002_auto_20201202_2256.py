# Generated by Django 3.1.4 on 2020-12-02 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_news',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 2, 22, 56, 40, 228560)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 2, 22, 56, 40, 229560)),
        ),
    ]