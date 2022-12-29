from django.urls import path
from .views import *


app_name = "crm_main"

urlpatterns = [
    path('', homepage, name='home'),

    path('about/', aboutpage, name='about')
]