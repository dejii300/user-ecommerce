# Generated by Django 4.1.4 on 2022-12-26 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0005_customer_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='User',
            new_name='user',
        ),
    ]