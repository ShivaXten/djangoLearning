# Generated by Django 4.2.15 on 2024-09-04 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_profile_date_of_birth_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
