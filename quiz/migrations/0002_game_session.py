# Generated by Django 5.0 on 2023-12-30 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sessions.session'),
        ),
    ]
