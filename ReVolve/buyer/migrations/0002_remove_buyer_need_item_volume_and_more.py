# Generated by Django 5.0.6 on 2024-06-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer_need',
            name='item_volume',
        ),
        migrations.AddField(
            model_name='buyer_need',
            name='item_dimension',
            field=models.CharField(max_length=50, null=True),
        ),
    ]