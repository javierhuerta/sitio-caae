# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0010_contactpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(default='Esta es la descripcion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='subtitle',
            field=models.CharField(default='Envianos un Email', max_length=255),
            preserve_default=False,
        ),
    ]
