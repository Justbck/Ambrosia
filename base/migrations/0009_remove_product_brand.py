# Generated by Django 3.1.7 on 2021-04-14 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20210413_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
