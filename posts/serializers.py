from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    """Turn the objects in database into JSON"""

    class Meta:
        model = Posts
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        

class UserSerializer(serializers.ModelSerializer):
    """Turn objects in database into JSON"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)