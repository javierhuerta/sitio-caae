# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0039_auto_20151012_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkfields',
            name='link_external_title',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
