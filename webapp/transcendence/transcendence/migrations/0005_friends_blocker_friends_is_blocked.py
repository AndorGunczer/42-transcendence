# Generated by Django 5.1.1 on 2024-09-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0004_users2_is_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='blocker',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='friends',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
