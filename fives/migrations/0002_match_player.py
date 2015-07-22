# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Date')),
                ('home_goals', models.IntegerField(null=True)),
                ('away_goals', models.IntegerField(null=True)),
                ('match_details', models.TextField(max_length=500)),
                ('away_team', models.ForeignKey(related_name='+', to='fives.Team')),
                ('home_team', models.ForeignKey(related_name='+', to='fives.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('birthday', models.DateField()),
            ],
        ),
    ]
