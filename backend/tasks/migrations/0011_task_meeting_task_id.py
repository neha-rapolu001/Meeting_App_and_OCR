# Generated by Django 4.2.5 on 2024-11-24 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_rename_is_delete_task_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='meeting_task_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]