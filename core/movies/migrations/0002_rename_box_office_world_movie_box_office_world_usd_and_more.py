# Generated by Django 5.0 on 2023-12-22 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='box_office_world',
            new_name='box_office_world_usd',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='run_time',
            new_name='run_time_min',
        ),
        migrations.RenameField(
            model_name='userrating',
            old_name='rating',
            new_name='user_rating',
        ),
    ]