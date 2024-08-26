from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from .models import Users2, MsgHistory


# def index(request):
#     return HttpResponse("Hello, world. You're at index.")

def index(request):
	users = Users2.objects.raw('select * from transcendence_users2')
	# with connection.cursor() as cursor:
	# 	cursor.execute('select Username from transcendence_users2',)
	# 	usernames = cursor.fetchall()
	context = {'users': users}
	return render(request, "index.html", context)


def dialog(request, receiver):
	try:
		sender_obj = Users2.objects.get(username='placeholder')
	except Users2.DoesNotExist:
		return HttpResponse("Sender not found", status=404)
	try:
		receiver_obj = Users2.objects.get(username=receiver)
	except Users2.DoesNotExist:
		return HttpResponse("Receiver not found", status=404)
	# [sender_obj] = Users2.objects.raw('select * from transcendence_users2 where username = %s', ['placeholder'])
	sender_id = sender_obj.id
	# [receiver_obj] = Users2.objects.raw('select * from transcendence_users2 where username = %s', [receiver])
	receiver_id = receiver_obj.id
	msgs = Users2.objects.raw('select * from chat_msghistory where sender_id =%s AND receiver_id =%s', [sender_id, receiver_id])
	# with connection.cursor() as cursor:
	# 	cursor.execute('select Username from transcendence_users2',)
	# 	usernames = cursor.fetchall()
	context = {'msgs': msgs, 'receiver': receiver}
	return render(request, "dialog.html", context)

def send(request):
	receiver=request.GET.get('receiver')
	text=request.GET.get('msg')
	try:
		sender_obj = Users2.objects.get(username='placeholder')
	except Users2.DoesNotExist:
		return HttpResponse("Sender not found", status=404)
	try:
		receiver_obj = Users2.objects.get(username=receiver)
	except Users2.DoesNotExist:
		return HttpResponse("Receiver not found", status=404)
	# [sender_obj] = Users2.objects.raw('select * from transcendence_users2 where username = %s', ['placeholder'])
	sender_id = sender_obj.id
	# [receiver_obj] = Users2.objects.raw('select * from transcendence_users2 where username = %s', [receiver])
	receiver_id = receiver_obj.id
	MsgHistory.objects.create(sender=sender_obj, receiver=receiver_obj, msg=text)
	return JsonResponse({})
# Create your views here.
