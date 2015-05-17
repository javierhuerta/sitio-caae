# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0016_linkfields_second_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkfields',
            name='second_level',
        ),
        migrations.AddField(
            model_name='menu',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='second_level',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
