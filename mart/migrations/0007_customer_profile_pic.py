# Generated by Django 4.1.4 on 2022-12-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0006_rename_user_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
