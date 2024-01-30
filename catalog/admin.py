from django.contrib import admin

from catalog.models import Product, Category, Contact, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'item_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Version)
class VersiojAdmin(admin.ModelAdmin):
    list_display = ('name', 'version_number', 'product', 'is_active')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'ind_number',)
    list_filter = ('name', 'address')
    search_fields = ('name', 'email')
