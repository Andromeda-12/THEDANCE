from django.db import models


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


class Client(models.Model):
    Name = models.CharField(max_length=150)
    Birthdate = models.DateField()
    Passport = models.CharField(max_length=12)
    Phone = models.CharField(max_length=13)
    Email = models.EmailField()
    Login = models.CharField(max_length=50)
    Password = models.CharField(max_length=24)


class Style(models.Model):
    Name = models.CharField(max_length=50)
    TreinerID = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Price = models.PositiveIntegerField()
    Description = models.TextField()
    clients = models.ManyToManyField(Client)


class Schedule(models.Model):
    StyleID = models.ForeignKey(Style, on_delete=models.CASCADE)
    Weekday = models.CharField(max_length=2)
    Time = models.TimeField()


class Payment(models.Model):
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    StyleID = models.ForeignKey(Style, on_delete=models.CASCADE)
    Cost = models.IntegerField()
    Payment_date = models.DateField()


# field = models.{field_type}('name_of_field', max_lenght, e.t.c.)
# def __str__(self):
#     return self.field, e.t.c.

# python manage.py makemigrations
# do migrations ->
#     python manage.py migrate

# python manage.py createsuperuser

#   class Meta:
#       verbose_mane = 'Учитель'
#       verbose_name_plural = 'Учителя'
