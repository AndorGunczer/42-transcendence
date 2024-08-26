from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from transcendence.models import Users2

# Create your models here.
class Blocked(models.Model):
	id = models.BigAutoField(primary_key=True)
	user = models.ForeignKey(Users2, on_delete=models.CASCADE, related_name='user')
	blocked = models.ForeignKey(Users2, on_delete=models.CASCADE, related_name='blocked')

class MsgHistory(models.Model):
	id = models.BigAutoField(primary_key=True)
	sender = models.ForeignKey(Users2, on_delete=models.CASCADE, related_name='sender')
	receiver = models.ForeignKey(Users2, on_delete=models.CASCADE, related_name='receiver')
	msg = models.CharField(max_length=224)
	timestamp = models.DateTimeField(auto_now=True)

