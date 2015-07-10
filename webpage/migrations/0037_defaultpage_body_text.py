# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0036_homepage_programs_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultpage',
            name='body_text',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
