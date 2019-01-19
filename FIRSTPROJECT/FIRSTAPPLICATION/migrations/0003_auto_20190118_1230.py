# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0002_auto_20190118_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
