# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0010_auto_20150715_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name='away', to='fives.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home', to='fives.Team'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='team',
            field=models.ForeignKey(related_name='player', to='fives.Team', null=True),
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
