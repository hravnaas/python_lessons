# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
        ('courses', '0002_auto_20160917_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(related_name='courses', to='login_reg.User'),
        ),
    ]
