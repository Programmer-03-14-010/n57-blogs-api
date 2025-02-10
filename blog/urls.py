from django.urls import path
from .views import PostListCreateView
from django.urls import path
from .views import home, PostListCreateView


urlpatterns = [
path('', home, name='home'),
    path('api/v1/posts/', PostListCreateView.as_view(), name='post-list-create'),
]
