# Generated by Django 5.1 on 2024-11-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='best_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_src', models.URLField()),
                ('last_episode_date', models.CharField(max_length=50)),
                ('criticScore', models.IntegerField()),
                ('audienceScore', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='best_tv_show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_src', models.URLField()),
                ('last_episode_date', models.CharField(max_length=50)),
                ('criticScore', models.IntegerField()),
                ('audienceScore', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='new_movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_src', models.URLField()),
                ('last_episode_date', models.CharField(max_length=50)),
                ('criticScore', models.IntegerField()),
                ('audienceScore', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='new_tv_show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_src', models.URLField()),
                ('last_episode_date', models.CharField(max_length=50)),
                ('criticScore', models.IntegerField()),
                ('audienceScore', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='popular_on_hbo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_src', models.URLField()),
                ('last_episode_date', models.CharField(max_length=50)),
                ('criticScore', models.IntegerField()),
                ('audienceScore', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='soon_in_theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_src', models.URLField()),
                ('last_episode_date', models.CharField(max_length=50)),
                ('criticScore', models.IntegerField()),
                ('audienceScore', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
