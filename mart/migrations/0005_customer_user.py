# Generated by Django 4.1.4 on 2022-12-26 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mart', '0004_tag_order_customer_order_product_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='User',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
