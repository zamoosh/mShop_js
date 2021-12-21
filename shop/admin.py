from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "description")
    list_per_page = 10


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_header = 'Main menu'
admin.site.site_title = 'Admin panel for Shop'
admin.site.index_title = 'admin panel'
