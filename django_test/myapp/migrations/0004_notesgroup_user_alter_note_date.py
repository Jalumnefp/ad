# Generated by Django 4.2.7 on 2023-12-02 14:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_alter_note_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesgroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 12, 2, 14, 25, 24, 349084, tzinfo=datetime.timezone.utc)),
        ),
    ]
