# Generated by Django 4.2.1 on 2023-05-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_voter_id_delete_cricketplayers'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoterId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Voter_Id',
        ),
    ]
