# Generated by Django 3.2.21 on 2024-02-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_profile_years_of_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='years_of_experience',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
