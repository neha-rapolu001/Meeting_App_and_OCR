# Generated by Django 4.2.5 on 2024-03-23 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0003_alter_church_id'),
        ('requestuser', '0003_alter_requestuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestuser',
            name='church',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='church.church'),
        ),
        migrations.AlterField(
            model_name='requestuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]