from django.contrib import admin
from .models import Teacher
from .models import Client
from .models import Style
from .models import Schedule
from .models import Payment

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Client)
admin.site.register(Style)
admin.site.register(Schedule)
admin.site.register(Payment)
