# Generated by Django 5.0.3 on 2024-11-18 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_value_db_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='value_db',
            name='mail',
            field=models.EmailField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
