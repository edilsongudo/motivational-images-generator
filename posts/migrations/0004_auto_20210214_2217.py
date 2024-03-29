# Generated by Django 3.0 on 2021-02-14 20:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210214_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='brand_name_font_size',
            field=models.IntegerField(blank=True, default=100, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brightness',
            field=models.IntegerField(blank=True, default=20, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='line_separation',
            field=models.IntegerField(blank=True, default=100, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo_size',
            field=models.IntegerField(blank=True, default=100, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_font_size',
            field=models.IntegerField(blank=True, default=100, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
