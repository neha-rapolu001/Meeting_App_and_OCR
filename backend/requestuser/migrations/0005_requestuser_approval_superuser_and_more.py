# Generated by Django 4.2.5 on 2024-03-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requestuser', '0004_alter_requestuser_church_alter_requestuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestuser',
            name='Approval_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestuser',
            name='deny_status',
            field=models.BooleanField(default=False),
        ),
    ]
