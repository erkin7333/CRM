from django.urls import path
from .views import *

app_name = 'crm_core'

urlpatterns = [
    path('add-lead/', add_lead, name='add_lead'),

    path('leads/', LeadListView.as_view(), name='leads'),

    path('lead-detail/<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),

    path('lead-edit/<int:pk>/', LeadUpdateView.as_view(), name='edit'),

    path('<int:pk>/convert', convert_to_client, name='convert'),

    path('<int:pk>/', lead_delete, name='delete'),

    path('<int:pk>/add-comment/', AddCommentView.as_view(), name='add_comment'),

    path('<int:pk>/add-file/', AddFileView.as_view(), name='add_file')
]