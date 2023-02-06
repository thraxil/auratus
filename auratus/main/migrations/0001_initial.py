# flake8: noqa
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'no title', max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default=b'')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AlbumPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album', models.ForeignKey(to='main.Album', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'no title', max_length=256)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('taken', models.DateTimeField(null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('views', models.IntegerField(default=0)),
                ('reticulum_key', models.CharField(default=b'', max_length=256)),
                ('extension', models.CharField(default=b'jpg', max_length=256)),
            ],
            options={
                'ordering': ['-uploaded'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhotoTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ForeignKey(to='main.Photo', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=256)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='phototag',
            name='tag',
            field=models.ForeignKey(to='main.Tag', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albumphoto',
            name='photo',
            field=models.ForeignKey(to='main.Photo', on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterOrderWithRespectTo(
            name='albumphoto',
            order_with_respect_to='album',
        ),
    ]
