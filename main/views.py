from django.shortcuts import render, redirect
from .models import *


def index(request):
    teacher = Teacher.objects.all()
    client = Client.objects.all()
    return render(request, 'main/index.html',
                  {"teachers": teacher, "clients": client})


def login(request):
    global current_user
    if request.method == "POST":
        worker = Teacher.objects.get(Login=request.POST.get("w_login"), Password=request.POST.get("w_password"))
        client = Client.objects.get(Login=request.POST.get("c_login"), Password=request.POST.get("c_password"))
        if len(client) > 0 and len(worker) == 0:
            current_user = client
        elif len(worker) > 0 and len(client) == 0:
            current_user = worker
        redirect('main/login.html', {"user": current_user})
    return render(request, 'main/login.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        birthdate = request.POST.get("date")
        passport = request.POST.get("passport")
        phone = request.POST.get("phone")
        mail = request.POST.get("email")
        new_client = Client.objects.create(Name=name, Birthdate=birthdate, Passport=passport, Phone=phone, Email=mail,
                                           Login=mail, Password=passport)
        new_client.save()
    return render(request, 'main/register.html')


def client_info(request, id):
    lesson = list()
    client = Client.objects.get(id=id)
    courses = Style.objects.filter(clients__id=id)
    for item in courses:
        lesson = (Schedule.objects.filter(Style=item))
    print(lesson)
    return render(request, 'main/client.html', {"user": client, "styles": courses, "lessons": lesson})


def worker_info(request, id):
    lesson = list()
    worker = Teacher.objects.get(id=id)
    courses = Style.objects.filter(Treiner__id=id)
    for item in courses:
        lesson = (Schedule.objects.filter(Style=item))
    print(lesson)
    return render(request, 'main/worker.html', {"user": worker, "styles": courses, "lessons": lesson})


def timetable(request):
    return render(request, 'main/timetable.html')