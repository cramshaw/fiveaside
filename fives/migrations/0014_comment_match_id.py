# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='match_id',
            field=models.ForeignKey(default=1, to='fives.Match'),
            preserve_default=False,
        ),
    ]
