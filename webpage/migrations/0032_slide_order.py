# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0031_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
    ]
