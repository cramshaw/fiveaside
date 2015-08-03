# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fives', '0016_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='available_players',
            field=models.ManyToManyField(related_name='player', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
