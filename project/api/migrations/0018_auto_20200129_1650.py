# Generated by Django 3.0.2 on 2020-01-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_review_ips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ips',
            field=models.CharField(max_length=100),
        ),
    ]
