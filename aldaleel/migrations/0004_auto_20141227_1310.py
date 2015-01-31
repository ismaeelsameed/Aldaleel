# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldaleel', '0003_auto_20141227_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255, null=True)),
                ('address', models.CharField(default=b'', max_length=255, null=True)),
                ('area', models.CharField(default=b'', max_length=255, null=True)),
                ('phone', models.CharField(default=b'', max_length=255, null=True)),
                ('image', models.ImageField(upload_to=b'company_images')),
                ('price', models.CharField(default=b'', max_length=255, null=True)),
                ('notes', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('company', models.ForeignKey(to='aldaleel.Company', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='arabic_name',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='english_name',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
