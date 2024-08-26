from django.contrib import admin

# Register your models here.
from .models import Blocked
from .models import MsgHistory

admin.site.register(Blocked)
admin.site.register(MsgHistory)