# Generated by Django 5.0.6 on 2024-06-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=200)),
                ('item_material_type', models.CharField(max_length=100)),
                ('item_grade', models.CharField(max_length=50)),
            ],
        ),
    ]
