# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldaleel', '0002_auto_20141225_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
        migrations.AddField(
            model_name='company',
            name='arabic_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='english_name',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'company_logos', blank=True),
            preserve_default=True,
        ),
    ]
