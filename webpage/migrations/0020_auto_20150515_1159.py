# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('webpage', '0019_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_page',
            field=models.ForeignKey(related_name='about_+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose the about page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_text',
            field=wagtail.wagtailcore.fields.RichTextField(default='hola'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.EmailField(default='javierhuerta@unach.cl', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='facebook',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='gallery_page',
            field=models.ForeignKey(related_name='gallery_+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose the gallery page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='instagram',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='phone',
            field=models.CharField(default='sdfsd', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='twiter',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
