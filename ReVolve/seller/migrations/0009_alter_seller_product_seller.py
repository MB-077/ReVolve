# Generated by Django 5.0.6 on 2024-06-08 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_remove_seller_seller_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='seller.seller'),
        ),
    ]
