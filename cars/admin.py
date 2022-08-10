from django.contrib import admin
from .models import car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border_radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'
    list_display_links = ('id','thumbnail','car_title')
    search_fields = ('car_title','model','body_style','fuel_type', 'is_featured','city')
    list_display = ('id','thumbnail','car_title', 'color','city', 'model', 'year', 'body_style','fuel_type', 'is_featured')
    list_editable = ('is_featured',)
    list_filter = ('city','model','body_style')
admin.site.register(car,CarAdmin)
