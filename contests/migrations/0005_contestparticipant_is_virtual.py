# Generated by Django 5.1.4 on 2024-12-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_contest_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestparticipant',
            name='is_virtual',
            field=models.BooleanField(default=False),
        ),
    ]
