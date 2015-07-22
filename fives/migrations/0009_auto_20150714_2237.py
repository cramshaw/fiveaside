# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0008_match_is_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='birthday',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
