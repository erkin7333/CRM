from django.contrib import admin
from .models import Client, Comment, ClientFile
from django.utils.html import format_html


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


class ClientFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'client', 'image_tag', 'created_by', 'created_at')
    list_display_links = ('id', 'team', 'client',)

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.files.url))
    readonly_fields = ('image_tag', )
    class Meta:
        model = ClientFile

admin.site.register(ClientFile, ClientFileAdmin)