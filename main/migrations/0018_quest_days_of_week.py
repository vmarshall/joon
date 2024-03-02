# Generated by Django 4.2.10 on 2024-03-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_recurringschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='days_of_week',
            field=models.CharField(blank=True, choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], help_text='Days of the week to repeat the quest', max_length=3, verbose_name='Days of the week'),
        ),
    ]
