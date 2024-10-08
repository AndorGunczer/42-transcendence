# Generated by Django 5.1 on 2024-09-06 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0002_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=128)),
                ('receiver', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=256)),
                ('friendship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcendence.friends')),
            ],
        ),
    ]
