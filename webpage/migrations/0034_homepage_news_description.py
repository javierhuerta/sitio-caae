# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0033_auto_20150629_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='news_description',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
