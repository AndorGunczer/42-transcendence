# Generated by Django 5.0.4 on 2024-05-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0002_alter_users_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]