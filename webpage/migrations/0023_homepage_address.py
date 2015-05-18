# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0022_auto_20150518_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(default='por ahi', max_length=255),
            preserve_default=False,
        ),
    ]
