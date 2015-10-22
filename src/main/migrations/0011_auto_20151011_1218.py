# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20151011_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film_actor',
            name='actor_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='film_actor',
            name='film_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='staff_id',
            field=models.IntegerField(),
        ),
    ]
