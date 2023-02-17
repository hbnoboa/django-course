
import os

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.pagination import make_pagination

from .models import Recipe

PER_PAGES = int(os.environ.get('PER_PAGE', 2))


def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    page_obj, pagination_range, previous_page, next_page = make_pagination(
        request, recipes, PER_PAGES)

    return render(request, 'recipes/pages/index.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'previous_page': previous_page,
        'next_page': next_page,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_published=True).order_by('-id'))

    page_obj, pagination_range, previous_page, next_page = make_pagination(
        request, recipes, PER_PAGES)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'previous_page': previous_page,
        'next_page': next_page,
        'title': f'{recipes[0].category.name} - Categoria |'
    })


def recipe(request, id):

    recipe = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
        'title': f'{recipe.category.name}'
    })


def search(request):
    search_term = request.GET.get('q')

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(title__icontains=search_term) |
        Q(description__icontains=search_term),
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range, previous_page, next_page = make_pagination(
        request, recipes, PER_PAGES)

    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'{ search_term }',
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'previous_page': previous_page,
        'next_page': next_page,
        'additional_url_query': f'&q={search_term}'
    })
