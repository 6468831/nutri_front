from django.urls import path

from .views import (
    RecipeListView,
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe_list'),
    # path('', update_recipe_list_ajax.as_view(), name='update_recipe_list'),
]
