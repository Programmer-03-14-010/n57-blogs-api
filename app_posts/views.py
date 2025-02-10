from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

from app_posts.models import PostsModel


@api_view(["GET", "POST"])
def posts_view(request):
    if request.method == "GET":
        posts = PostsModel.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serialize = PostSerializer(data=request.POST)
        if serialize.is_valid():
            serialize.save()
            return Response(data=serialize.data, status=status.HTTP_201_CREATED)
        return Response(data=serialize.data, status=status.HTTP_400_BAD_REQUEST)



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            return self.queryset.filter(user_id=user)
        return self.queryset
