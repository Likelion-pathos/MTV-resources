# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    # author = serializers.ReadOnlyField(source = 'author.username')
    created_at = serializers.DateTimeField(format='%y.%m.%d', read_only=True)

    class Meta:
        model = Post
        fields = [ 'id', 'title', 'content', 'author', 'created_at' ]

        
