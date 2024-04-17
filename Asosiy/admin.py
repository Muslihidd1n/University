from django.contrib import admin

from .models import *

"4 masala"


class UstozAdmin(admin.ModelAdmin):
    list_display = ["id","ism","jins","yosh","daraja","fan"]
    search_fields = ["ism"]
    search_help_text = "ismi boyicha qidirish"

"5 masala"

class YonalishAdmin(admin.ModelAdmin):
    list_display = ["nom","aktiv"]
    list_filter = ["aktiv"]
    search_fields = ["nom"]
    search_help_text = "Qidirish"


"6 masala"

class FanAdmin(admin.ModelAdmin):
    list_display = ["nom","yonalish","asosiy"]
    search_fields = ["nom"]
    search_help_text = "Qdiruv"
    list_filter = ["asosiy","yonalish"]


admin.site.register(Yonalish)
admin.site.register(Ustoz)
admin.site.register(Fan)