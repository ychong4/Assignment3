from django.conf.urls import url
from . import views
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

app_name = 'pethome'
urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('donate/', views.donate, name='donate'),
    path('dogs/', views.dogs, name='dogs'),
    path('cats/', views.cats, name='cats'),
]