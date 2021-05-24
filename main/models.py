from django.db import models
from django.urls import reverse


# Create your models here.
# Создаем новый класс. Например, Учителя
class Teacher(models.Model):
    # create new field
    Name = models.CharField(max_length=150)
    Birthdate = models.DateField()
    Education_certificate = models.PositiveIntegerField()
    Profession = models.CharField(max_length=100)
    Home = models.CharField(max_length=200)
    Login = models.CharField(max_length=50)
    Password = models.CharField(max_length=24)

    def get_absolute_url(self):
        return reverse('worker', kwargs={'id': self.id})


class Client(models.Model):
    Name = models.CharField(max_length=150)
    Birthdate = models.DateField()
    Passport = models.CharField(max_length=12)
    Phone = models.CharField(max_length=13)
    Email = models.EmailField()
    Login = models.CharField(max_length=50)
    Password = models.CharField(max_length=24)

    def get_absolute_url(self):
        return reverse('client', kwargs={'id': self.id})


class Style(models.Model):
    Name = models.CharField(max_length=50)
    Treiner = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    Price = models.PositiveIntegerField()
    Description = models.TextField()
    clients = models.ManyToManyField(Client)


class Schedule(models.Model):
    Style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True)
    Weekday = models.CharField(max_length=2)
    Time = models.TimeField()


class Payment(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    Style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True)
    Cost = models.IntegerField()
    Payment_date = models.DateField()
