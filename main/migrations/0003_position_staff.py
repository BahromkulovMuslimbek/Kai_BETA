# Generated by Django 5.1.1 on 2024-09-12 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_position_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.staff'),
        ),
    ]