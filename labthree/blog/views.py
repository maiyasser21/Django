from http.client import ResponseNotReady
from urllib import response
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets,mixins
from rest_framework.response import Response
from blog.models import Post,Comment
from blog.serializers import BlogSerializer,CommentSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class GenericPostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    
class GenericUpdatePostList(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=BlogSerializer
    
class CreateListRetrievViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset=Post.objects.all()
    serializer_class=BlogSerializer
    
class CommentListCreateView(generics.ListCreateAPIView):
    # queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
    def get_queryset(self):
        current_user_post=Post.objects.filter(owner=self.request.user)
        return Comment.objects.filter(owner=self.request.user)
    
    









# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer = BlogSerializer   
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = BlogSerializer
#         return Response({'status': 'success', 'message': 'Posts retrieved successfully!', 'posts': serializer.data})
    
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'status': 'success', 'message': 'Post retrieved successfully!', 'post': serializer.data})
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response({'status': 'success', 'message': 'Post created successfully!', 'post': serializer.data['id']}, status=status.HTTP_201_CREATED, headers=headers)
         
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response({'status': 'success', 'message': 'Post updated successfully!', 'post': serializer.data['id']})
    
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({'status': 'success', 'message': 'Post deleted successfully!'})
    
    
