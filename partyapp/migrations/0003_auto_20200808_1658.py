# Generated by Django 3.0.7 on 2020-08-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partyapp', '0002_auto_20200808_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]