from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Room, Message
from django.http import JsonResponse, request, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def base(request):
    return render(request, "base.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class home(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "home.html"


def get(self, request):
    return HttpResponse('room')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {

        'username': username,
        'room': room,
        'room_details': room_details,
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect("/" + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect("/" + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
