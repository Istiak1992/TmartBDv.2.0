# Generated by Django 4.1.6 on 2023-02-04 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_product_product_image_productimage_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catgory_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
