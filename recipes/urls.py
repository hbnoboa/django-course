from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
