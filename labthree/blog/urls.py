from django.contrib import admin
from django.urls import path
from blog.views import GenericPostList,GenericUpdatePostList,CreateListRetrievViewSet,CommentListCreateView

urlpatterns = [
   path("genericapi",GenericPostList.as_view()),
   path("updateposts/<int:pk>",GenericUpdatePostList.as_view(), {'http_method': 'PUT'}),
   path('deleteposts/<int:pk>/delete/', GenericUpdatePostList.as_view(), {'http_method': 'DELETE'}),
   path('test/',CreateListRetrievViewSet.as_view({'get':"list",'post':'create'})),
   path('commentsOnpost',CommentListCreateView.as_view()),
]