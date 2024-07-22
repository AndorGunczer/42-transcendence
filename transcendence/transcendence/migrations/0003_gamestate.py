# Generated by Django 4.2.13 on 2024-07-18 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcendence', '0002_users2_allow_otp_users2_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball_x', models.FloatField(default=600.0)),
                ('ball_y', models.FloatField(default=300.0)),
                ('ball_speed_x', models.FloatField(default=7.5)),
                ('ball_speed_y', models.FloatField(default=7.5)),
                ('ball_direction_x', models.IntegerField(default=1)),
                ('ball_direction_y', models.IntegerField(default=1)),
                ('paddle1_y', models.FloatField(default=262.5)),
                ('paddle2_y', models.FloatField(default=262.5)),
                ('game_running', models.BooleanField(default=False)),
                ('countdown', models.IntegerField(default=3)),
                ('winning_score', models.IntegerField(default=1)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='transcendence.games')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
