# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0006_auto_20190118_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phn_num',
            field=models.CharField(unique=True, max_length=264),
        ),
    ]
