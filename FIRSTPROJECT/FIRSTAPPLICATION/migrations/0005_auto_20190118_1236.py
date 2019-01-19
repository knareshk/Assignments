# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPPLICATION', '0004_auto_20190118_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name_id',
            new_name='name',
        ),
    ]
