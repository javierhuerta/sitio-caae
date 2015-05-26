# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0025_program_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='body_personalize',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
