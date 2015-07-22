# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0002_match_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.AddField(
            model_name='match',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 6, 21, 20, 59, 460224, tzinfo=utc), verbose_name=b'time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='away_goals',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_goals',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_details',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
