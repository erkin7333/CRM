from django.urls import path
from .views import *

app_name = 'crm_core'

urlpatterns = [
    path('add-lead/', add_lead, name='add_lead')
]