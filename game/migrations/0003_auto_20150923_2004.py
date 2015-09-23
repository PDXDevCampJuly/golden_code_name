# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20150923_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.AddField(
            model_name='board',
            name='guesses_allowed',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='board',
            name='is_blue',
            field=models.BooleanField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='card',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='card',
            name='word',
            field=models.CharField(max_length=50, default=None),
        ),
        migrations.AddField(
            model_name='clue',
            name='clue',
            field=models.CharField(max_length=50, default=None),
        ),
        migrations.AddField(
            model_name='clue',
            name='num_of_cards',
            field=models.PositiveSmallIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='team',
            name='is_blue',
            field=models.BooleanField(default=True, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='team',
            name='spies_left',
            field=models.PositiveSmallIntegerField(default=None),
        ),
    ]
