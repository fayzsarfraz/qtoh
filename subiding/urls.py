from django.urls import path
from . import views  # what is the meaning of this thing when we write .
from django.contrib import admin

urlpatterns = [
    path('', views.index,  name='subiding'),

]
