# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-02 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luck', '0005_remove_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bidcount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
