# Generated by Django 3.2.7 on 2021-09-29 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210929_0458'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='Car',
        ),
    ]