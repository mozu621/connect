# Generated by Django 4.0.2 on 2022-06-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_portfolio_tag_tag_tagportfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]