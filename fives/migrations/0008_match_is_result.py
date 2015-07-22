# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0007_auto_20150714_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_result',
            field=models.BooleanField(default=False),
        ),
    ]
