# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0001_initial'),
        ('wagtailforms', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtailsearch', '0001_initial'),
        ('webpage', '0021_auto_20150518_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='from_address',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='subject',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactpage',
            name='to_address',
            field=models.CharField(help_text='Optional - form submissions will be emailed to this address', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formfield',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='form_fields', to='webpage.ContactPage'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
