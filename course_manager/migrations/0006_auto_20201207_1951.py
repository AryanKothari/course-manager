# Generated by Django 3.1 on 2020-12-07 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0005_auto_20201207_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_time',
        ),
    ]
