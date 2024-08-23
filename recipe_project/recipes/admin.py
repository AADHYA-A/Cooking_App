from django.contrib import admin

# Register your models here.
# recipes/admin.py
from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'preparation_time')
    search_fields = ('title', 'ingredients')
    ordering = ('title',)
