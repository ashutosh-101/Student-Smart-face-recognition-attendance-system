# Generated by Django 3.0.8 on 2020-07-26 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceapp', '0003_indlist_encoded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orgattendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgname', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='Userattendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
