# Generated by Django 5.1.4 on 2025-01-13 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0007_favoritecontest'),
        ('problems', '0008_submissiontestresult'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='contestproblem',
            constraint=models.UniqueConstraint(fields=('contest', 'problem'), name='unique_contest_problem'),
        ),
    ]