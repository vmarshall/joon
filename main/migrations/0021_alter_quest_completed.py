# Generated by Django 4.2.10 on 2024-03-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_quest_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
