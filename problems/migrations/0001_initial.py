# Generated by Django 5.1.4 on 2024-12-23 15:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Код')),
            ],
        ),
        migrations.CreateModel(
            name='SubmissionStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('NP', 'PENDING'), ('OK', 'ACCEPTED'), ('RJ', 'REJECTED'), ('CE', 'COMPILATION_ERROR'), ('RE', 'RUNTIME_ERROR'), ('PE', 'PRESENTATION_ERROR'), ('WA', 'WRONG_ANSWER'), ('TL', 'TIME_LIMIT_EXCEEDED'), ('ML', 'MEMORY_LIMIT_EXCEEDED'), ('AW', 'AWAITING_MANUAL'), ('RM', 'REJECTED_MANUAL'), ('BA', 'BANNED')], default='NP', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('input_format', models.TextField()),
                ('output_format', models.TextField()),
                ('time_limit', models.IntegerField(default=1)),
                ('memory_limit', models.IntegerField(default=256)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='problems', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='problems.problemtag')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=35)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('execution_time', models.FloatField(blank=True, null=True)),
                ('memory_used', models.FloatField(blank=True, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.submissioncontent')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.submissionstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdin', models.TextField()),
                ('expected_output', models.TextField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
            ],
        ),
    ]