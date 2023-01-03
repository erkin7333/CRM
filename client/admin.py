from django.contrib import admin
from .models import Client



class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'description',
                    'created_by', 'created_at', 'modified_at')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'description')
    class Meta:
        model = Client
admin.site.register(Client, ClientAdmin)
