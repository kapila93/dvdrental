# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151011_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city_id',
            field=models.ForeignKey(to='main.city'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country_id',
            field=models.ForeignKey(to='main.country'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address_id',
            field=models.ForeignKey(to='main.address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='store_id',
            field=models.ForeignKey(to='main.store'),
        ),
        migrations.AlterField(
            model_name='film_actor',
            name='actor_id',
            field=models.ForeignKey(to='main.actor'),
        ),
        migrations.AlterField(
            model_name='film_actor',
            name='film_id',
            field=models.ForeignKey(to='main.film'),
        ),
        migrations.AlterField(
            model_name='film_category',
            name='category_id',
            field=models.ForeignKey(to='main.category'),
        ),
        migrations.AlterField(
            model_name='film_category',
            name='film_id',
            field=models.ForeignKey(to='main.film'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='film_id',
            field=models.ForeignKey(to='main.film'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='store_id',
            field=models.ForeignKey(to='main.store'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_id',
            field=models.ForeignKey(to='main.customer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='rental_id',
            field=models.ForeignKey(to='main.rental'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='staff_id',
            field=models.ForeignKey(to='main.staff'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='customer_id',
            field=models.ForeignKey(to='main.customer'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='inventory_id',
            field=models.ForeignKey(to='main.inventory'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='staff_id',
            field=models.ForeignKey(to='main.staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_id',
            field=models.ForeignKey(to='main.address'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='store_id',
            field=models.ForeignKey(to='main.store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='address_id',
            field=models.ForeignKey(to='main.address'),
        ),
        migrations.AlterField(
            model_name='store',
            name='manager_staff_id',
            field=models.ForeignKey(to='main.staff'),
        ),
    ]
