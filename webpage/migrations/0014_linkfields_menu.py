# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0013_gallerypage_gallerypagepicturelist'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkfields',
            name='menu',
            field=models.ForeignKey(blank=True, to='webpage.Menu', null=True),
            preserve_default=True,
        ),
    ]
