# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from game.models import Word
from django.db import models, migrations


def populate_dict(apps, schema_editor):
    wordlist = ['woodcraft', 'woodcraft', 'woodcut', 'wooded', 'woof', 'wool',
                'woozy', 'word', 'work', 'world', 'worm',
                'vegetable', 'vehement', 'vehicle', 'version', 'versus',
                'vertigo', 'very', 'vesicle', 'vestige',
                'veto', 'vet', 'vex', 'via', 'vial', 'vibes', 'vibrant',
                'Emergent', 'delavan', 'palladized', 'noncorporeal',
                'parasynthesis', 'cancellation', 'uncourteousness', 'salishan',
                'unrequested', 'resistance',
                'avoirdupois', 'muhlenberg', 'hygienic', 'Nonjudicatory',
                'scenography', 'impartibility', 'unrounded',
                'thermography', 'diffusibility', 'diplomacy', 'filate',
                'stringy']
    for phrase in wordlist:
        theword = Word(word=phrase)
        theword.save()


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_dict),
    ]
