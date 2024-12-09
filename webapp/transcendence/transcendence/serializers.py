
# Serializers (For validation)

from rest_framework import serializers
from asgiref.sync import sync_to_async
import bleach

def sanitize_input(value):
    return bleach.clean(value, tags=[], attributes={}, strip=True)

class BaseUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        return sanitize_input(value)
    def validate_password(self, value):
        return sanitize_input(value)

class RegistrationSerializer(BaseUserSerializer):
    email = serializers.EmailField()
    avatar = serializers.CharField(max_length=255, required=False)
    twofa = serializers.BooleanField(required=False)

    def validate_email(self, value):
        return sanitize_input(value)

class LoginSerializer(BaseUserSerializer):
    pass

class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    avatar = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=255)

    def validate_username(self, value):
        return sanitize_input(value)


from transcendence.models import Players, Games, Users2

# Serializer for incoming data (player1 and player2)
class LocalGameRequestSerializer(serializers.Serializer):
    player1 = serializers.CharField(max_length=150)
    player2 = serializers.CharField(max_length=150)

    def validate_player1(self, value):
        return sanitize_input(value)
    def validate_player2(self, value):
        return sanitize_input(value)

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

    def validate_tournament_name(self, value):
        return sanitize_input(value)
    def validate_players(self, players):
        # Sanitize each player's name
        sanitized_players = [sanitize_input(player) for player in players]

        # Check for duplicates
        if len(sanitized_players) != len(set(sanitized_players)):
            raise serializers.ValidationError("Players list cannot contain duplicates.")

        return sanitized_players

class FriendRequestSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=150)

    def validate_receiver(self, value):
        sanitized_value = sanitize_input(value)
        # Additional custom validation for the receiver if needed
        if not sync_to_async(Users2.objects.filter(username=sanitized_value).exists)():
            raise serializers.ValidationError("Receiver does not exist")
        return sanitized_value

class MessageSerializer(serializers.Serializer):
    friendship_id = serializers.IntegerField()
    sender = serializers.CharField(max_length=150)
    receiver = serializers.CharField(max_length=150)
    message = serializers.CharField()

    # Input sanitization for each field
    def validate_sender(self, value):
        return sanitize_input(value)

    def validate_receiver(self, value):
        return sanitize_input(value)

    def validate_message(self, value):
        return sanitize_input(value)

    def validate_friendship_id(self, value):
        if value < 0:
            raise serializers.ValidationError("Invalid friendship ID.")
        return value

    # Creating the message instance
    def create(self, validated_data):
        # Import models inside the method to avoid potential circular imports
        from .models import Messages, Friends, Users2

        # Validate if friendship exists and is not blocked
        friendship = Friends.objects.get(id=validated_data['friendship_id'])
        if friendship.is_blocked:
            raise serializers.ValidationError("Friendship is blocked.")

        sender = Users2.objects.get(username=validated_data['sender'])
        receiver = Users2.objects.get(username=validated_data['receiver'])

        # Create the message using the sanitized and validated data
        return Messages.objects.create(
            friendship=friendship,
            sender=sender.username,
            receiver=receiver.username,
            message=validated_data['message']
        )