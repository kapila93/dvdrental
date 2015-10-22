# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20151011_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='language_id',
            field=models.ForeignKey(to='main.language'),
        ),
    ]
