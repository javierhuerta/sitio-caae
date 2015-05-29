# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('webpage', '0026_aboutpage_body_personalize'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=75, null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TallerPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('time', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('room', models.CharField(max_length=255)),
                ('number', models.PositiveIntegerField()),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('photo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('team', models.ForeignKey(to='webpage.Program')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='personlist',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='person_list', to='webpage.TallerPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personlist',
            name='person',
            field=models.ForeignKey(related_name='+', to='webpage.Person'),
            preserve_default=True,
        ),
    ]
