# Generated by Django 4.0.4 on 2022-04-21 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pronat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address_line',
            field=models.CharField(default=True, help_text='E nevojeshme', max_length=255, verbose_name='Adresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='district_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pronat.district'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
