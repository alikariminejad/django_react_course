# Generated by Django 4.2.7 on 2025-07-18 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
