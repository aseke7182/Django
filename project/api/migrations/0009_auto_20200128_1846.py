# Generated by Django 3.0.2 on 2020-01-28 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200128_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Company'),
        ),
    ]