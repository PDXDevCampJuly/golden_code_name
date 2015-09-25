# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('is_revealed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('hint', models.CharField(max_length=50, default=None)),
                ('number', models.PositiveSmallIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('color', models.CharField(max_length=2, choices=[('bl', 'Blue Team'), ('rd', 'Red Team'), ('bg', 'Bystander'), ('bk', 'Assassin')])),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('current_turn', models.ForeignKey(to='game.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('spies_left', models.PositiveSmallIntegerField(blank=True)),
                ('color_id', models.ForeignKey(to='game.Color')),
                ('game_id', models.ForeignKey(to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word', models.CharField(serialize=False, max_length=50, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='clue',
            name='game_id',
            field=models.ForeignKey(to='game.Game'),
        ),
        migrations.AddField(
            model_name='clue',
            name='team_id',
            field=models.ForeignKey(to='game.Team'),
        ),
        migrations.AddField(
            model_name='card',
            name='color_id',
            field=models.ForeignKey(to='game.Color'),
        ),
        migrations.AddField(
            model_name='card',
            name='game_id',
            field=models.ForeignKey(to='game.Game'),
        ),
        migrations.AddField(
            model_name='card',
            name='word_id',
            field=models.ForeignKey(to='game.Word'),
        ),
    ]
