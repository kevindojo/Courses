# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
    ]
