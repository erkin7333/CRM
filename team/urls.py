from django.urls import path
from .views import *

app_name = 'team'

urlpatterns = [
    path('edit/<int:pk>/', edit_team, name='edit_name')
]