# Generated by Django 3.0 on 2021-02-24 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_profile_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='money',
            field=models.FloatField(default=0.0),
        ),
    ]
