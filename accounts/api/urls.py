from django.urls import path, include
from  accounts.api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')

app_name='accounts'



urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('', include(router.urls)),
]