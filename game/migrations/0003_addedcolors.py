# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from game.models import Color
from django.db import models, migrations


def create_color(apps, schema_editor):
    Color(color='bg').save()
    Color(color='bl').save()
    Color(color='rd').save()
    Color(color='bk').save()

class Migration(migrations.Migration):
    dependencies = [
        ('game', '0002_addwordsdatabase'),
    ]


    operations = [
        migrations.RunPython(create_color),
    ]
