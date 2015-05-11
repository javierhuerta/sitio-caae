# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_aboutpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='sub_title',
            field=models.CharField(default='subtitulo', max_length=255),
            preserve_default=False,
        ),
    ]
