# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_auto_20150511_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='last_name',
        ),
    ]
