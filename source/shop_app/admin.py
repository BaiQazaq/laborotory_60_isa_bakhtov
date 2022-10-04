from django.contrib import admin

from shop_app.models import Good

# Register your models here.

class GoodAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "photo", "category", "balance", "price",  "created_at")
    list_filter = ("id", "title", "description", "price", "category", "balance", "created_at")
    search_fields = ("title", "price", "category")
    fields = ("title", "description", "created_at", "changed_at")
    readonly_fields = ("id", "created_at", "changed_at")

admin.site.register(Good, GoodAdmin)

