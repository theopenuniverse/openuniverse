# Generated by Django 2.1.2 on 2018-11-01 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('owner', models.TextField()),
                ('owner_type', models.TextField()),
                ('updated_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('application_domain', models.TextField()),
                ('software_license', models.TextField()),
                ('age', models.IntegerField()),
                ('main_language', models.TextField()),
                ('github_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFeatures',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.Project')),
                ('has_contributing', models.BooleanField()),
                ('has_readme', models.BooleanField()),
                ('has_wiki', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatistics',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.Project')),
                ('pulls_merged_total', models.IntegerField()),
                ('newcomers_total', models.IntegerField()),
                ('open_issues_total', models.IntegerField()),
                ('used_languages_total', models.IntegerField()),
                ('forks_total', models.IntegerField()),
                ('stars_total', models.IntegerField()),
                ('commits_total', models.IntegerField()),
                ('contributors_total', models.IntegerField()),
                ('core_members_total', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='timeseries',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Project'),
        ),
    ]
