# Generated by Django 3.2.19 on 2023-09-07 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mini_chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='participants',
        ),
        migrations.AddField(
            model_name='conversation',
            name='user1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='conversations1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conversation',
            name='user2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='conversations2', to=settings.AUTH_USER_MODEL),
        ),
    ]
