from django.contrib import admin
from django.urls import path
from authors.views import *

urlpatterns = [

    path('', list_authors),
    path('<name>',view_author),
    path('JKRowling/HarryPotter',view_harrypotter),
    
]
