# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0016_auto_20160411_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvelog',
            name='approve_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approve_log', to='customers.PendingApprove'),
        ),
    ]
