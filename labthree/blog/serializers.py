from rest_framework import serializers
from blog.models import Post,Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    owner=serializers.CharField(source="owner.username")
    class Meta:
        model=Comment
        fields=['owner','body','post','created_on']
    