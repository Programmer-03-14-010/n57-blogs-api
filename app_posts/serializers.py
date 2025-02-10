from rest_framework import  serializers
from .models import Product

from app_posts.models import PostsModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostsModel
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'slug', 'created_at']