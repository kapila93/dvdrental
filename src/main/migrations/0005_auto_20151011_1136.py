# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_store_manager_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='replacement_cost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.FloatField(),
        ),
    ]
