from django.urls import path
from polls import views
urlpatterns = [
    path('',views.view_allquestions),
    path('<int:question_id>',views.view_question,name="question_details"),
    path('create',views.create),
    path('delete/<question_id>',views.delete, name="delete"),
]