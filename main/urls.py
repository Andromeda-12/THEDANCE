from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.sing_in, name='sing_in'),
    path('client-<str:login>', views.client_info, name='client')
]
