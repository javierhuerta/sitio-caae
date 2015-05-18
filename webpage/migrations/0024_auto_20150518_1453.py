# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('webpage', '0023_homepage_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='icon_class',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='program',
            name='related_page',
            field=models.ForeignKey(related_name='gallery_+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Select a page related', null=True),
            preserve_default=True,
        ),
    ]
