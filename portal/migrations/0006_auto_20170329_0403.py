# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_question_is_recommeded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='recommended_answer',
            field=models.TextField(null=True),
        ),
    ]
