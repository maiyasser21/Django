from django.urls import path
from users.views import *

urlpatterns = [
    path('login_user', login_user,name="login"),
    path('logout_user',logout_user, name='logout'),
]