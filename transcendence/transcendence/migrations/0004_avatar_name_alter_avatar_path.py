# Generated by Django 4.2.13 on 2024-06-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0003_rename_picture_avatar_rename_pictures_users2_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='name',
            field=models.CharField(default='Not Set', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='path',
            field=models.CharField(default='Not Set', max_length=150, unique=True),
        ),
    ]
