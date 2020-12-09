# Generated by Django 3.1.4 on 2020-12-03 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0012_auto_20201203_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_news_new',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 22, 32, 37, 45399)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='time_comment',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 3, 22, 32, 37, 47396)),
        ),
        migrations.AlterField(
            model_name='profile_settings',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='uploads'),
        ),
    ]
