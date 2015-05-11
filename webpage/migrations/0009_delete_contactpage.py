# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0008_auto_20150511_1435'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactPage',
        ),
    ]
