# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0003_auto_20190118_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phn_num',
            field=models.IntegerField(unique=True, max_length=264),
        ),
    ]
