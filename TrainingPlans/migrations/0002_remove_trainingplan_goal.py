# Generated by Django 5.0.6 on 2024-06-10 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrainingPlans', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingplan',
            name='goal',
        ),
    ]
