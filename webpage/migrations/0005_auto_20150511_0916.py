# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('webpage', '0004_team_teampage_teampageteamlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='image',
        ),
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
    ]
