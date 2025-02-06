# Generated by Django 5.1.5 on 2025-02-05 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_student_password_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='other_user_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_no', models.CharField(max_length=50)),
                ('residence', models.TextField(blank=True, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
