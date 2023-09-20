
from django.urls import path

from .views import (
    FoodDataView, FoodCategoryList,
    CategoryFoodsView, FoodMaxNutrientsView,
    CompareFoodsView,
    )

from .views_ajax import (
    get_food_data_for_comparison_ajax,
)


urlpatterns = [
    path('', FoodCategoryList.as_view(), name='food_category_list'),
    path('category_<slug:category_slug>/', CategoryFoodsView.as_view(), name='food_category'),
    path('<slug:primary_slug>-vs-<slug:secondary_slug>/', CompareFoodsView.as_view(), name='compare_foods'),
    path('max_<slug:nutrient_slug>/', FoodMaxNutrientsView.as_view(), name='max_nutrients'),
    path('get_food_data_for_comparison/', get_food_data_for_comparison_ajax, name='get_food_data_for_comparison'),
    path('<slug:food_slug>/', FoodDataView.as_view(), name='food'),
]
