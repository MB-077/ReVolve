# Generated by Django 5.0.6 on 2024-06-09 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0013_seller_seller_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='seller_name',
            new_name='seller_username',
        ),
    ]
