# Generated by Django 4.1.5 on 2023-01-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_category_photo_maincategory_photo_subcategory_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/Cataegory/'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/MainCataegory/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/Products/'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/SubCataegory/'),
        ),
    ]
