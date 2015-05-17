# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0015_defaultpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkfields',
            name='second_level',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
