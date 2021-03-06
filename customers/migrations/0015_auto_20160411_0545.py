# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-11 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_otheraccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvelog',
            name='create_date',
        ),
        migrations.AddField(
            model_name='approvelog',
            name='approve_info',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='approve_log', to='customers.PendingApprove'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pendingapprove',
            name='create_date',
            field=models.DateTimeField(auto_now=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='approvelog',
            name='action_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
