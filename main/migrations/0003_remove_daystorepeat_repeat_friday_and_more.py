# Generated by Django 5.0.2 on 2024-03-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_daystorepeat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_friday',
        ),
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_monday',
        ),
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_saturday',
        ),
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_sunday',
        ),
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_thursday',
        ),
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_tuesday',
        ),
        migrations.RemoveField(
            model_name='daystorepeat',
            name='repeat_wednesday',
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='friday',
            field=models.BooleanField(default=False, help_text='Repeat on Friday'),
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='monday',
            field=models.BooleanField(default=False, help_text='Repeat on Monday'),
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='saturday',
            field=models.BooleanField(default=False, help_text='Repeat on Saturday'),
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='sunday',
            field=models.BooleanField(default=False, help_text='Repeat on Sunday'),
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='thursday',
            field=models.BooleanField(default=False, help_text='Repeat on Thursday'),
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='tuesday',
            field=models.BooleanField(default=False, help_text='Repeat on Tuesday'),
        ),
        migrations.AddField(
            model_name='daystorepeat',
            name='wednesday',
            field=models.BooleanField(default=False, help_text='Repeat on Wednesday'),
        ),
    ]
