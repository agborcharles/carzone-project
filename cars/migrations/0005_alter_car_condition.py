# Generated by Django 3.2.7 on 2021-09-29 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.TextField(max_length=200),
        ),
    ]