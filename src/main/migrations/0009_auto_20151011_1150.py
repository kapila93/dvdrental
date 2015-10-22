# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151011_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
