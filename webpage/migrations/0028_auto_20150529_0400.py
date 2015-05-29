# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0027_auto_20150529_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tallerpage',
            name='team',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='webpage.Program', null=True),
            preserve_default=True,
        ),
    ]
