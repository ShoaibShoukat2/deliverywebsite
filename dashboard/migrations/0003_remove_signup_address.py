# Generated by Django 5.0.3 on 2024-04-07 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_signup_remember_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='address',
        ),
    ]
