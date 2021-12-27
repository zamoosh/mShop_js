from django.contrib import admin
from .models import *


class ProductAdminInline(admin.TabularInline):
    model = Product
    extra = 2


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [ProductAdminInline]


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Product info", {"fields": ["name"]}),
        ("Product price", {"fields": ["price"]}),
        ("Product category", {"fields": ["category"]}),
        ("Product description", {"fields": ["description"]}),
        ("Product photo", {"fields": ["picture"]}),
    ]
    list_display = ["name", "price", "category", "description"]
    list_editable = ["description", "category"]
    ordering = ["price", "name"]
    list_per_page = 4


class ShoppingCartAdmin(admin.ModelAdmin):
    fieldsets = [
        ("cart user", {"fields": ["user"]}),
        ("cart products", {"fields": ["product"]}),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.site_header = 'Main menu'
admin.site.site_title = 'Admin panel for Shop'
admin.site.index_title = 'admin panel'
