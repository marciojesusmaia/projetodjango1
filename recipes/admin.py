from django.contrib import admin
from .models import Category, Recipe
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    
    ...

#outra forma de fazer
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
