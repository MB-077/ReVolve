# Generated by Django 5.0.6 on 2024-06-08 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_alter_seller_product_item_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_id',
            field=models.CharField(auto_created=True, max_length=50, unique=True),
        ),
    ]