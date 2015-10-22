# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151011_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
