# Generated by Django 4.0.2 on 2022-05-19 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tag_portfolio_content_profile_introduction_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tagname',
        ),
    ]
