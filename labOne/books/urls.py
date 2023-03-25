from django.contrib import admin
from django.urls import path
from books.views import *

urlpatterns = [

    path('<name>', hello),
    
]
