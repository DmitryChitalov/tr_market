# Generated by Django 3.0.3 on 2021-09-07 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210907_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 9, 16, 2, 24, 372100)),
        ),
    ]