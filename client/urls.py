from django.urls import path
from .views import *


app_name = "client"

urlpatterns = [
    path('client/', client_list, name='client'),

    path('client/<int:pk>/', client_detail, name='client_detail')
]