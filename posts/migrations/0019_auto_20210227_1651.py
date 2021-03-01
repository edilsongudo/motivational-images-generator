# Generated by Django 3.0 on 2021-02-27 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20210227_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='brand_name',
            field=models.CharField(default='@yourbrandname', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brand_name_font_color',
            field=models.CharField(default='#ffffff', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brand_name_font_size',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brand_name_font_type',
            field=models.CharField(choices=[('BebasNeue Bold', 'BebasNeue Bold'), ('BebasNeue Book', 'BebasNeue Book'), ('big_noodle_titling_oblique', 'big_noodle_titling_oblique'), ('big_noodle_titling', 'big_noodle_titling'), ('BRADHITC', 'BRADHITC'), ('CHILLER', 'CHILLER'), ('COLONNA', 'COLONNA'), ('comic', 'comic'), ('comicbd', 'comicbd'), ('cordia', 'cordia'), ('cordiab', 'cordiab'), ('cordiai', 'cordiai'), ('cordiau', 'cordiau'), ('cordiaub', 'cordiaub'), ('cordiaui', 'cordiaui'), ('cordiauz', 'cordiauz'), ('CURLZ___', 'CURLZ___'), ('FORTE', 'FORTE'), ('FREESCPT', 'FREESCPT'), ('FRSCRIPT', 'FRSCRIPT'), ('Gabriola', 'Gabriola'), ('HARNGTON', 'HARNGTON'), ('JOKERMAN', 'JOKERMAN'), ('MISTRAL', 'MISTRAL'), ('PRISTINA', 'PRISTINA'), ('RAGE', 'RAGE'), ('segoepr', 'segoepr'), ('segoeprb', 'segoeprb')], default='big_noodle_titling_oblique', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brightness',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Portuguese', 'Portuguese')], default='English', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_image_downloaded',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='profile',
            name='line_separation',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo_size',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_of_posts_created',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number_of_posts_downloaded',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_font_size',
            field=models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_font_type',
            field=models.CharField(choices=[('BebasNeue Bold', 'BebasNeue Bold'), ('BebasNeue Book', 'BebasNeue Book'), ('big_noodle_titling_oblique', 'big_noodle_titling_oblique'), ('big_noodle_titling', 'big_noodle_titling'), ('BRADHITC', 'BRADHITC'), ('CHILLER', 'CHILLER'), ('COLONNA', 'COLONNA'), ('comic', 'comic'), ('comicbd', 'comicbd'), ('cordia', 'cordia'), ('cordiab', 'cordiab'), ('cordiai', 'cordiai'), ('cordiau', 'cordiau'), ('cordiaub', 'cordiaub'), ('cordiaui', 'cordiaui'), ('cordiauz', 'cordiauz'), ('CURLZ___', 'CURLZ___'), ('FORTE', 'FORTE'), ('FREESCPT', 'FREESCPT'), ('FRSCRIPT', 'FRSCRIPT'), ('Gabriola', 'Gabriola'), ('HARNGTON', 'HARNGTON'), ('JOKERMAN', 'JOKERMAN'), ('MISTRAL', 'MISTRAL'), ('PRISTINA', 'PRISTINA'), ('RAGE', 'RAGE'), ('segoepr', 'segoepr'), ('segoeprb', 'segoeprb')], default='big_noodle_titling_oblique', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='primary_text_color',
            field=models.CharField(default='#ffffff', max_length=30),
        ),
    ]