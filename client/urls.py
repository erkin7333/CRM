from django.urls import path
from .views import *


app_name = "client"

urlpatterns = [
    path('client/', ClientListView.as_view(), name='client'),

    path('add-client/', client_add, name='add_client'),

    path('edit/<int:pk>/', edit_client, name='edit_client'),

    path('delete/<int:pk>/', client_delete, name='delete'),

    path('client/<int:pk>/', client_detail, name='client_detail'),

    path('add-comment/<int:pk>/', client_detail, name='add_comment'),

    path('<int:pk>/add-file/', client_add_file, name='add_file'),

    path('export/', client_export, name='export')
]