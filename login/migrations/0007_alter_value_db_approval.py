# Generated by Django 5.0.3 on 2024-11-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_value_db_national_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value_db',
            name='approval',
            field=models.IntegerField(default=1),
        ),
    ]