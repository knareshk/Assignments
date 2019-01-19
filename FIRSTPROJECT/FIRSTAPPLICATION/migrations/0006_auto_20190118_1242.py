# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0005_auto_20190118_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='name_id',
        ),
        migrations.RenameField(
            model_name='name',
            old_name='id',
            new_name='name_id',
        ),
    ]
