# Generated by Django 3.1.2 on 2024-12-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20241221_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat_class',
            field=models.CharField(choices=[('economy', 'Phổ thông'), ('business', 'Business'), ('first', 'First')], max_length=20),
        ),
    ]