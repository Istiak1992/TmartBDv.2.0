# Generated by Django 4.1.6 on 2023-02-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
