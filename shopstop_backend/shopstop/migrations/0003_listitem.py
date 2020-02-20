# Generated by Django 3.0.3 on 2020-02-14 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopstop', '0002_auto_20200212_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of the item')),
                ('quantity', models.IntegerField(default=1, verbose_name='How many of the item to get')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopstop.List')),
            ],
        ),
    ]
