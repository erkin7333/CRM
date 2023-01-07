from django.contrib import admin
from .models import *
from django.utils.html import format_html


admin.site.register(Lead)
admin.site.register(Comment)




class LeadFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'lead', 'image_tag', 'created_by', 'created_at')
    list_display_links = ('id', 'team', 'lead',)

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.files.url))
    readonly_fields = ('image_tag', )
    class Meta:
        model = LeadFile

admin.site.register(LeadFile, LeadFileAdmin)