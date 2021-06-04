from django.urls import path, re_path
from . import views
from .views import UserCount

urlpatterns = (
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('client/<str:id>', views.client_info, name='client'),
    path('worker/<str:id>', views.worker_info, name='worker'),
    path('timetable', views.timetable, name='timetable'),
    path('get-user-count/', UserCount.as_view(), name= 'get-user-count')
)
