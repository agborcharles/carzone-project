from django.contrib import admin
from . models import *
from django.utils.html import format_html
# Register your models here.

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="60" />'.format(obj.car_photo.url))
    thumbnail.short_description = 'Photo'

    list_display = ['id', 'thumbnail', 'car_title', 'state', 'color',
                    'is_feautred', 'model', 'year']
    #search_fields = ['customer', ]
    list_per_page = 400
    search_fields = ('car_title', 'state', 'model',)
    list_filter = ('car_title',)
    list_display_links = ('car_title', 'state', 'model', 'thumbnail',)
    list_editable = ('is_feautred',)

admin.site.register(Car, CarAdmin)
