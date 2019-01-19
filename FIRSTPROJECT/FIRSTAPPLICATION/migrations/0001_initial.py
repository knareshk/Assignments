# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('addr', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phn_num', models.CharField(unique=True, max_length=264)),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=264)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.ForeignKey(to='FIRSTAPPLICATION.Name'),
        ),
        migrations.AddField(
            model_name='address',
            name='details',
            field=models.ForeignKey(to='FIRSTAPPLICATION.Contact'),
        ),
    ]
