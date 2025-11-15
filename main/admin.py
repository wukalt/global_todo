from django.contrib import admin
from django.utils.html import mark_safe
from .models import Priority, Event


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ["name", "color", "icon"]

    def color_display(self, obj):
        return mark_safe(f"<div style='width: 20px; height: 20px; background-color: {obj.color}; border-radius: 4px;'></div>")
    color_display.short_description = "Color"

    def icon_display(self, obj):
        return mark_safe(f"<i class='{obj.icon}' style='font-size:20px;'></i>")
    icon_display.short_description = "Icon"


admin.site.register(Event)