from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='scratcher-home'),
    path("about/", views.about, name='scratcher-about')


]