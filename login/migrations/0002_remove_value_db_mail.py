# Generated by Django 5.0.3 on 2024-11-18 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value_db',
            name='mail',
        ),
    ]