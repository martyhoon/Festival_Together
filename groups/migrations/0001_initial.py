# Generated by Django 2.1 on 2019-11-29 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('leader_id', models.CharField(default='', max_length=20)),
                ('festival_name', models.CharField(default='', max_length=30)),
                ('festival_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateField(default=datetime.date.today)),
                ('hashtag', models.CharField(default='', max_length=30)),
                ('usercount', models.IntegerField(blank=True, default=0, null=True)),
                ('maxcount', models.IntegerField(blank=True, default=1, null=True)),
                ('ticket', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(default='', max_length=200)),
                ('is_authenticated', models.IntegerField(default=0)),
            ],
        ),
    ]
