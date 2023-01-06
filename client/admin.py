from django.contrib import admin
from .models import Client, Comment



class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'description', 'team',
                    'created_by', 'created_at', 'modified_at')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'description')
    class Meta:
        model = Client
admin.site.register(Client, ClientAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'client', 'content', 'created_by', 'created_at')
    list_display_links = ('id', 'team', 'client')
    class Meta:
        model = Comment
admin.site.register(Comment, CommentAdmin)