# Generated by Django 3.0.3 on 2021-09-01 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210901_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 3, 16, 6, 18, 463847)),
        ),
    ]
