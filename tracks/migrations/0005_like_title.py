# Generated by Django 3.0.4 on 2020-04-02 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0004_remove_like_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='title',
            field=models.CharField(default=datetime.datetime.now, max_length=50),
        ),
    ]
