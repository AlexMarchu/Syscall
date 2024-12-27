# Generated by Django 5.1.4 on 2024-12-27 09:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problems', '0006_problem_visible_tests_count'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField()),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContestParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants_info', to='contests.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contests_participations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contest',
            name='participants',
            field=models.ManyToManyField(related_name='contests', through='contests.ContestParticipant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ContestProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='contests.contest')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contests', to='problems.problem')),
            ],
        ),
        migrations.CreateModel(
            name='ContestSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='contests.contestparticipant')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_submissions', to='problems.submission')),
            ],
        ),
    ]
