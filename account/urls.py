from django.urls import path
from .views import *
from django.contrib.auth import views


app_name = "account"

urlpatterns = [
    path('sign-up/', signup, name='signup'),

    path('login/', views.LoginView.as_view(template_name='account/login.html'), name='login'),

    path('myaccount/', myaccount, name='myaccount'),

    path('log-out/', views.LogoutView.as_view(), name='logout')
]