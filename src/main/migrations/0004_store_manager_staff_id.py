# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151011_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='manager_staff_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
