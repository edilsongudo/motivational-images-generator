# Generated by Django 3.0 on 2021-03-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passwordsmanager', '0006_auto_20210314_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterpassword',
            name='master',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]