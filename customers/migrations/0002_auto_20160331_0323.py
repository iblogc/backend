# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='account_id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.RemoveField(
            model_name='company',
            name='alias_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='examine_id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='company',
            name='legal_name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='legal_thumb',
        ),
        migrations.RemoveField(
            model_name='company',
            name='license',
        ),
        migrations.RemoveField(
            model_name='company',
            name='license_thumb',
        ),
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='company',
            name='province',
        ),
        migrations.RemoveField(
            model_name='company',
            name='status',
        ),
        migrations.RemoveField(
            model_name='company',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='company',
            name='thumb',
        ),
        migrations.RemoveField(
            model_name='company',
            name='update_time',
        ),
        migrations.RemoveField(
            model_name='company',
            name='website',
        ),
        migrations.RemoveField(
            model_name='company',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='company',
            name='no',
            field=models.IntegerField(default=0),
        ),
    ]
