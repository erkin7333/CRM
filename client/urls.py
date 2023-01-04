from django.urls import path
from .views import *


app_name = "client"

urlpatterns = [
    path('client/', client_list, name='client'),

    path('add-client/', client_add, name='add_client'),

    path('client/<int:pk>/', client_detail, name='client_detail')
]