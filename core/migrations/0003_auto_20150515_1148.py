# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailsearch', '0001_initial'),
        ('core', '0002_create_homepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]
