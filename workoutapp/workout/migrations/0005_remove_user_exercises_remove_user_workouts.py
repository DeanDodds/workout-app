# Generated by Django 4.1.3 on 2022-11-28 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_remove_user_exercise_remove_user_workout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='exercises',
        ),
        migrations.RemoveField(
            model_name='user',
            name='workouts',
        ),
    ]
