# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import block.models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_auto_20141011_2223'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('date_moderated', models.DateTimeField(null=True, blank=True)),
                ('order', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('picture', models.ImageField(upload_to='block/main/%Y/%m/%d', blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Main content',
                'verbose_name_plural': 'Main contents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MainBlock',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('page_section', models.ForeignKey(to='block.PageSection')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='main',
            name='block',
            field=models.ForeignKey(related_name='content', to='web.MainBlock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='main',
            name='edit_state',
            field=models.ForeignKey(default=block.models._default_edit_state, to='block.EditState'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='main',
            name='moderate_state',
            field=models.ForeignKey(default=block.models._default_moderate_state, to='block.ModerateState'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='main',
            name='user_moderated',
            field=models.ForeignKey(related_name='+', null=True, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='main',
            unique_together=set([('block', 'moderate_state')]),
        ),
    ]
