from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms


@admin.register(Weapon)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type_of_weapon", "get_image")
    list_display_links = ("name",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="50"')

    get_image.short_description = "Изображение"


@admin.register(Case)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "get_image")
    list_display_links = ("name",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} height="50"')

    get_image.short_description = "Изображение"


# admin.site.register(WeaponLine)
admin.site.register(Rarity)
# admin.site.register(Case)
# admin.site.register(Weapon)
admin.site.register(TypeOfWeapon)
