# Generated by Django 4.0.4 on 2022-04-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pronat', '0002_property_address_line_property_district_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.IntegerField(),
        ),
    ]
