from django.contrib import admin

from .models import Dog, Cat

class DogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'breed', 'color', 'age', 'gender', 'size', 'weight', 'adoption_fee', 'description', 'image']
    list_filter = ['id', 'name', 'breed', 'color', 'age', 'gender', 'size', 'weight', 'adoption_fee', 'description', 'image']
    search_fields = ['id', 'name', 'breed', 'color', 'age', 'gender', 'size', 'weight', 'adoption_fee', 'description', 'image']
    model = Dog

class CatAdmin(admin.ModelAdmin):
    model = Cat


admin.site.register(Dog, DogAdmin)
admin.site.register(Cat, CatAdmin)
