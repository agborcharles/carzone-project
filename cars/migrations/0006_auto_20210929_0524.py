# Generated by Django 3.2.7 on 2021-09-29 04:24

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2020),
        ),
    ]
