# Generated by Django 3.0.2 on 2020-01-29 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200129_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='ips',
        ),
    ]