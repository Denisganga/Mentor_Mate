# Generated by Django 5.0.1 on 2024-03-14 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_profile_years_of_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=800)),
                ('image', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]
