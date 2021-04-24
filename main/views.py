from django.shortcuts import render

from main.models import Teacher
from main.models import Client


def index(request):
    teacher = Teacher.objects.all()
    client = Client.objects.all()
    return render(request, 'main/index.html', {"teachers": teacher, "clients": client})
