# Generated by Django 4.2.13 on 2024-07-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users2',
            name='allow_otp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users2',
            name='email',
            field=models.CharField(max_length=128, null=True),
        ),
    ]