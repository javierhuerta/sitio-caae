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
        ('webpage', '0037_defaultpage_body_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AlbumPagePictureList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='picture_list', to='webpage.AlbumPage')),
            ],
            options={
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GalleryPageAlbumList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('album', models.ForeignKey(related_name='+', to='webpage.AlbumPage')),
                ('page', modelcluster.fields.ParentalKey(related_name='album_list', to='webpage.GalleryPage')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PictureAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', wagtail.wagtailcore.fields.RichTextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='gallerypagepicturelist',
            name='page',
        ),
        migrations.RemoveField(
            model_name='gallerypagepicturelist',
            name='picture',
        ),
        migrations.DeleteModel(
            name='GalleryPagePictureList',
        ),
        migrations.RemoveField(
            model_name='picturegallery',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='picturegallery',
            name='program',
        ),
        migrations.DeleteModel(
            name='PictureGallery',
        ),
        migrations.AddField(
            model_name='albumpagepicturelist',
            name='picture',
            field=models.ForeignKey(related_name='+', to='webpage.PictureAlbum'),
            preserve_default=True,
        ),
    ]
