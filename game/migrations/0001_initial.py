# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Card__Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('card_desc', models.CharField(max_length=2, choices=[('bl', 'Blue Team'), ('rd', 'Red Team'), ('bg', 'Bystander'), ('bk', 'Assassin')])),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='clue',
            name='team',
            field=models.ForeignKey(to='game.Team'),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(to='game.Card__Type'),
        ),
    ]
