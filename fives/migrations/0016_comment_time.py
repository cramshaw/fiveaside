# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0015_auto_20150715_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 11, 46, 9, 289044, tzinfo=utc), verbose_name=b'time'),
            preserve_default=False,
        ),
    ]
