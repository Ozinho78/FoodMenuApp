from django.contrib import admin
from django.utils.html import format_html

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_price', 'image_preview')

    def image_preview(self, obj):
        if obj.item_image:
            return format_html('<img src="{}" style="height:36px;" />', obj.item_image.url)
        return "-"
    image_preview.short_description = "Vorschau"
