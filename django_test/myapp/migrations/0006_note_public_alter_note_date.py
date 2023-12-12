# Generated by Django 5.0 on 2023-12-12 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_note_favourite_alter_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 12, 8, 16, 9, 830097, tzinfo=datetime.timezone.utc)),
        ),
    ]
