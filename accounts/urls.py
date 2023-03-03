from django.urls import path
from . import views



urlpatterns = [
    path('login', views.login, name='login'),
     path('getprofile', views.get_profile, name='get_profile'),

]