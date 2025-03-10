# Generated by Django 5.1.5 on 2025-02-04 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='staff_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('staff_no', models.CharField(max_length=50, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('start_year', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
