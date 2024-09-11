import random
import string
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

def send_otp_via_email(user, otp):
    send_mail(
        'Your verification code',
        f'Your verification code is {otp}',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )

def verify_otp(user, otp):
    if user.otp_secret == otp:
        return True
    return False

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }