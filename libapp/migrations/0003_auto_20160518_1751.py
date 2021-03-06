# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('libitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='libapp.Libitem')),
                ('maker', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('rating', models.IntegerField(choices=[(1, 'G'), (2, 'PG'), (3, 'PG-13'), (4, '14A'), (5, 'R'), (6, 'NR')], default=1)),
            ],
            bases=('libapp.libitem',),
        ),
        migrations.RemoveField(
            model_name='libuser',
            name='age',
        ),
        migrations.AddField(
            model_name='libitem',
            name='num_chkout',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='libuser',
            name='postalcode',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
