from django.contrib import admin
from . models import *
from django.utils.html import format_html
# Register your models here.

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="60" style="border-radius: 300px;" />'.format(obj.photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ['id', 'thumbnail', 'first_name', 'last_name', 'description',
                    'facebook_link', 'google_link']
    #search_fields = ['customer', ]
    list_per_page = 400
    search_fields = ('first_name', 'last_name', 'description',)
    list_filter = ('description',)
    list_display_links = ('first_name', 'last_name', 'description', 'thumbnail')

admin.site.register(Team, TeamAdmin)
