from django.urls import path, include
from  like.api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'likes', views.LikeViewSet, basename='likes')


app_name='like'



urlpatterns = [
    path('', include(router.urls)),
]