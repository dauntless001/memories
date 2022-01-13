from django.urls import path
from  accounts.api import views


app_name='accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view()),
]