# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151011_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='rental_rate',
            field=models.FloatField(),
        ),
    ]
