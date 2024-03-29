# Generated by Django 4.1.4 on 2022-12-14 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0003_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mart.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mart.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='mart.tag'),
        ),
    ]
