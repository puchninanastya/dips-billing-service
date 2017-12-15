# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing_service', '0002_remove_payment_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Payment date'),
        ),
    ]
