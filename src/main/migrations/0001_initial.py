# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=20)),
                ('postal_code', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=50)),
                ('activebool', models.BooleanField()),
                ('create_date', models.DateField()),
                ('last_update', models.DateTimeField()),
                ('active', models.IntegerField()),
                ('address_id', models.ForeignKey(to='main.address')),
            ],
        ),
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('release_year', models.IntegerField()),
                ('rental_duration', models.IntegerField()),
                ('rental_rate', models.IntegerField()),
                ('length', models.IntegerField()),
                ('replacement_cost', models.IntegerField()),
                ('rating', models.CharField(max_length=10)),
                ('last_update', models.DateTimeField()),
                ('special_features', models.TextField()),
                ('fulltext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='film_actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField()),
                ('actor_id', models.ForeignKey(to='main.actor')),
                ('film_id', models.ForeignKey(to='main.film')),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField()),
                ('film_id', models.ForeignKey(to='main.film')),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('payment_date', models.DateTimeField()),
                ('customer_id', models.ForeignKey(to='main.customer')),
            ],
        ),
        migrations.CreateModel(
            name='rental',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rental_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
                ('customer_id', models.ForeignKey(to='main.customer')),
                ('inventory_id', models.ForeignKey(to='main.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=40)),
                ('last_update', models.DateTimeField()),
                ('picture', models.CharField(max_length=50)),
                ('address_id', models.ForeignKey(to='main.address')),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField()),
                ('address_id', models.ForeignKey(to='main.address')),
                ('manager_staff_id', models.ForeignKey(to='main.staff')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='store_id',
            field=models.ForeignKey(to='main.store'),
        ),
        migrations.AddField(
            model_name='rental',
            name='staff_id',
            field=models.ForeignKey(to='main.staff'),
        ),
        migrations.AddField(
            model_name='payment',
            name='rental_id',
            field=models.ForeignKey(to='main.rental'),
        ),
        migrations.AddField(
            model_name='payment',
            name='staff_id',
            field=models.ForeignKey(to='main.staff'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='store_id',
            field=models.ForeignKey(to='main.store'),
        ),
        migrations.AddField(
            model_name='film',
            name='language_id',
            field=models.ForeignKey(to='main.language'),
        ),
        migrations.AddField(
            model_name='customer',
            name='store_id',
            field=models.ForeignKey(to='main.store'),
        ),
        migrations.AddField(
            model_name='city',
            name='country_id',
            field=models.ForeignKey(to='main.country'),
        ),
        migrations.AddField(
            model_name='address',
            name='city_id',
            field=models.ForeignKey(to='main.city'),
        ),
    ]
