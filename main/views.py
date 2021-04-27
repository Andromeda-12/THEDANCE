from django.shortcuts import render

from main.models import *


def index(request):
    teacher = Teacher.objects.all()
    client = Client.objects.all()
    # if request.method == 'POST':
    #     role = request.POST.get("role")
    #     login = request.POST.get("login")
    #     password = request.POST.get("password")
    #     if role == "worker":
    #         user = Teacher()
    #         current_user = user.objects.get(Login=login, Password=password)
    #     elif role == "client":
    #         user = Client()
    #         current_user = user.objects.get(Login=login, Password=password)
    return render(request, 'main/index.html', {"teachers": teacher, "clients": client})


def sing_in(request):
    if request.method == 'POST':
        role = request.POST.get("role")
        login = request.POST.get("login")
        password = request.POST.get("password")
        if role == "worker":
            user = Teacher()
            current_user = user.objects.get(Login=login, Password=password)
        elif role == "client":
            user = Client()
            current_user = user.objects.get(Login=login, Password=password)
    return render(request, 'main/index.html', {"user": current_user})


def client_info(request):
    client = Client.objects.get(id=1)
    return render(request, 'main/client.html', {"client": client})
