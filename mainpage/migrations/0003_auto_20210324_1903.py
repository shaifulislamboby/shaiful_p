# Generated by Django 3.1.7 on 2021-03-24 19:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20210324_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailrecord',
            name='send_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 19, 3, 26, 359860, tzinfo=utc)),
        ),
    ]
