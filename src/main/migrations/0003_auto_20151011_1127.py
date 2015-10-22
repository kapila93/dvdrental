# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_film_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'city', 'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'country', 'verbose_name_plural': 'countries'},
        ),
        migrations.AlterModelOptions(
            name='film_category',
            options={'verbose_name': 'film category', 'verbose_name_plural': 'film categories'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'inventory', 'verbose_name_plural': 'inventories'},
        ),
        migrations.RemoveField(
            model_name='store',
            name='manager_staff_id',
        ),
        migrations.AlterField(
            model_name='address',
            name='city_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='city',
            name='country_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='store_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='film',
            name='language_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='film_category',
            name='category_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='film_category',
            name='film_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='film_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='store_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='rental_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='staff_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='customer_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='inventory_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='store_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='store',
            name='address_id',
            field=models.IntegerField(),
        ),
    ]
