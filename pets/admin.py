from django.contrib import admin
from .models import Category, Pet
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


def pet_detail(obj):
    url = reverse('pets:pet_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')

@admin.register(Pet)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'adoption_fee', 'available',
                     'created', 'updated', 'image', pet_detail]
    list_filter = ['available', 'category', 'created', 'updated' ]
    list_editable = ['adoption_fee', 'available']
    prepopulated_fields = {'slug': ('name',)}