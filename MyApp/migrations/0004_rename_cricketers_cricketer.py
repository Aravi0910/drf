# Generated by Django 4.2.1 on 2023-05-18 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_remove_cricketers_cricket_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cricketers',
            new_name='Cricketer',
        ),
    ]
