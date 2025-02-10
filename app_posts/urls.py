"""
users
posts
comments
post/likes
comment/likes

GET
    ADMIN
    /users/ -> users list
    /users/user_id/ -> user detail | GET, PUT, PATCH, DELETE

    USERS
    /users/ -> get own data | GET, PUT, PATCH, DELETE


----------------------

/api/v1/posts/ -> POST
/api/v1/posts/-> GET
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

app_name = "app_posts"  # app_name to'g'ri qo'yilishi kerak

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path("", include(router.urls)),
]
