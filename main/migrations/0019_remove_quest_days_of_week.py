# Generated by Django 4.2.10 on 2024-03-02 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_quest_days_of_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='days_of_week',
        ),
    ]
