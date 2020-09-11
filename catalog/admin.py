from django.contrib import admin
from .models import Category, Good


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Good, GoodAdmin)
