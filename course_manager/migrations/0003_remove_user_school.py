# Generated by Django 3.1 on 2020-12-07 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0002_user_school'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
    ]
