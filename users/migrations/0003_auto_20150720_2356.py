# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_expecteduser_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expecteduser',
            name='registration',
            field=models.CharField(unique=True, max_length=16, editable=False, blank=True),
        ),
    ]
