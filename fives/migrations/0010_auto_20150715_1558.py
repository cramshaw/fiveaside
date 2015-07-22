# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0009_auto_20150714_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'get_latest_by': 'time'},
        ),
    ]
