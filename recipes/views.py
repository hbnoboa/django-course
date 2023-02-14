from django.shortcuts import render

from utils.recipes.factory import make_recipe


def index(request):
    return render(request, 'recipes/pages/index.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipes': [make_recipe() for _ in range(1)],
        'is_detail_page': True,
    })
