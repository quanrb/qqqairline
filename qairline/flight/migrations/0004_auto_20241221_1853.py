# Generated by Django 3.1.2 on 2024-12-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20241221_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'NAM'), ('female', 'NỮ')], max_length=20),
        ),
    ]
