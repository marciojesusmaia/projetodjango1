from django.shortcuts import render
from recipes.utils.recipes.factory import make_recipe
from recipes.models import Recipe
from django.http import HttpResponse

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={'recipes': recipes})

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={'recipe': make_recipe(), 'is_detail_page':True,})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    if not recipes:
        return HttpResponse('Page Not Found', 404)
    return render(request, 'recipes/pages/category.html', context={'recipes':recipes, 'title': f'{recipes.first().category.name} - Category |'})

