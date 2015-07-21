# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expected_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expecteduser',
            name='registration',
            field=models.CharField(default=0, max_length=120, verbose_name=b'O60T2W'),
        ),
    ]
