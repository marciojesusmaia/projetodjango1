from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name':'Marcio Maia'})

def recipe(request):
    return render(request, 'recipes/pages/home.html')

