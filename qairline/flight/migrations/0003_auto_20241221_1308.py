# Generated by Django 3.1.2 on 2024-12-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20241221_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='business_fare',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='first_fare',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='coupon_discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='other_charges',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
