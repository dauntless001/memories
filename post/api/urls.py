from django.urls import path, include
from  post.api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')


app_name='post'



urlpatterns = [
    path('', include(router.urls)),
]