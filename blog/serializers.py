from rest_framework import serializers
from blog.models import Post
from django.utils import timezone


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'pub_date']

    
    