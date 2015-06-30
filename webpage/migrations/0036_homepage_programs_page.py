# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('webpage', '0035_programspage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='programs_page',
            field=models.ForeignKey(related_name='about_+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose the programs page', null=True),
            preserve_default=True,
        ),
    ]
