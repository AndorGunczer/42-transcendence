# Generated by Django 4.2.13 on 2024-07-05 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0005_alter_games_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='result',
            field=models.CharField(default='Not Set', max_length=100, null=True),
        ),
    ]
