from django.urls import path
from .views import *

app_name = 'crm_core'

urlpatterns = [
    path('add-lead/', add_lead, name='add_lead'),

    path('leads/', lead_list, name='leads'),

    path('lead-detail/<int:pk>/', lead_deteil, name='lead_detail'),

    path('lead-edit/<int:pk>/', edit_lead, name='edit'),

    path('<int:pk>/convert', convert_to_client, name='convert'),

    path('<int:pk>/', lead_delete, name='delete')
]