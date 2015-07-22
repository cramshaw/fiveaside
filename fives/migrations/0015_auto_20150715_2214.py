# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0014_comment_match_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='match_id',
            field=models.ForeignKey(related_name='comment', to='fives.Match'),
        ),
    ]
