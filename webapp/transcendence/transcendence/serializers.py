
# Serializers (For validation)

from rest_framework import serializers
from asgiref.sync import sync_to_async

class BaseUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

class RegistrationSerializer(BaseUserSerializer):
    email = serializers.EmailField()
    avatar = serializers.CharField(max_length=255, required=False)
    twofa = serializers.BooleanField(required=False)

class LoginSerializer(BaseUserSerializer):
    pass

class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    avatar = serializers.CharField(max_length=255)  # Assuming avatar is a URL, adjust if it's not

from transcendence.models import Players, Games, Users2

# Serializer for incoming data (player1 and player2)
class LocalGameRequestSerializer(serializers.Serializer):
    player1 = serializers.CharField(max_length=150)
    player2 = serializers.CharField(max_length=150)

# Serializer for Players model
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ['id', 'player', 'game', 'guest_name']

# Serializer for tournament creation
class TournamentCreateSerializer(serializers.Serializer):
    tournament_name = serializers.CharField(max_length=255)
    players = serializers.ListField(
        child=serializers.CharField(max_length=150),  # Each player is a string (username)
        min_length=2,  # Minimum number of players
        allow_empty=False
    )

class FriendRequestSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=150)

    def validate_receiver(self, value):
        # Additional custom validation for the receiver if needed
        if not sync_to_async(Users2.objects.filter(username=value).exists)():
            raise serializers.ValidationError("Receiver does not exist")
        return value