# Generated by Django 5.0.6 on 2024-06-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_seller_seller_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_contact',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
