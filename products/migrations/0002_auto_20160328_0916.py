# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_id',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='models', to='products.Product'),
        ),
    ]
