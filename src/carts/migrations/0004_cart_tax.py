# Generated by Django 3.0.5 on 2020-05-18 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=100),
        ),
    ]
