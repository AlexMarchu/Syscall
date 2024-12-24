# Generated by Django 5.1.4 on 2024-12-24 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_alter_problem_input_format_alter_problem_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='problems.problem'),
        ),
        migrations.AlterField(
            model_name='test',
            name='stdin',
            field=models.TextField(blank=True),
        ),
    ]