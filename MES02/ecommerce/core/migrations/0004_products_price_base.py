# Generated by Django 5.0.6 on 2024-05-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_products_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price_base',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]