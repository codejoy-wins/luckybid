# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-01-02 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luck', '0006_product_bidcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='winner',
            field=models.CharField(default='undecided', max_length=255, null=True),
        ),
    ]