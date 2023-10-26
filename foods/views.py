import requests

from django.shortcuts import render

from django.views import View
from django.conf import settings

from utils.services import get_base_url
from .services import (
    get_category_list, get_current_category,
    get_category_foods, get_food_list_to_compare,
    get_food_data, get_max_nutrient_food_list,
    get_compare_food_facts, get_child_categories
)

class FoodDataView(View):
    def get(self, request, food_slug):
        comparison_foods = get_food_list_to_compare(request)
        food = get_food_data(request, food_slug)
        menu_categories = get_category_list(request)
        context = {
            'food': food,
            'comparison_foods': comparison_foods,
            'menu_categories': menu_categories,
        }

        return render(request, 'foods/food_data.html', context)
    

class FoodCategoryList(View):
    def get(self, request):
        menu_categories = get_category_list(request)
        context = {
            'menu_categories': menu_categories,
        }
        return render(request, 'foods/food_category_list.html', context)
    

class CategoryFoodsView(View):
    def get(self, request, category_slug):
        current_category = get_current_category(request, category_slug)
        child_categories = get_child_categories(request, category_slug)
        food_categories = {}
        if child_categories != []:
            for child_category in child_categories:
                food_categories[child_category['name']] = get_category_foods(request, child_category['slug'])
        else:
            food_categories[current_category['name']] = get_category_foods(request, category_slug)
        menu_categories = get_category_list(request)

        context = {
            'current_category': current_category,
            'food_categories': food_categories,
            'menu_categories': menu_categories
        }
        
        return render(request, 'foods/food_category.html', context)
    

class FoodMaxNutrientsView(View):
    def get(self, request, nutrient_slug):
        foods = get_max_nutrient_food_list(request, nutrient_slug)
        menu_categories = get_category_list(request)

        context = {
            'foods': foods,
            'menu_categories': menu_categories,
        }

        return render(request, 'foods/max_nutrient.html', context)
    

class CompareFoodsView(View):
    def get(self, request, primary_slug, secondary_slug):
        primary_food = get_food_data(request, primary_slug)
        secondary_food = get_food_data(request, secondary_slug)
        compare_food_facts = get_compare_food_facts(
            request, 
            primary_slug, 
            secondary_slug
            )
        
        primary_food_nutrients = primary_food['food_nutrients']
        secondary_food_nutrients = secondary_food['food_nutrients']
        all_food_nutrients = list(zip(primary_food_nutrients, secondary_food_nutrients))

        comparison_foods = get_food_list_to_compare(request)
        import json
        print('!!', json.dumps(all_food_nutrients, indent=2))
        context = {
            'primary_food': primary_food,
            'secondary_food': secondary_food,
            'compare_food_facts': compare_food_facts,
            'all_food_nutrients': all_food_nutrients,
            'comparison_foods': comparison_foods
        }

        return render(request, 'foods/food_comparison.html', context)
    

class CompareFoodsListPageView(View):
    def get(self, request, food_slug):
        foods = get_food_list_to_compare(request, food_slug)
        menu_categories = get_category_list(request)
        
        context = {
            'foods': foods,
            'menu_categories': menu_categories,
            'food_slug': food_slug
        }

        return render(request, 'foods/compare_foods_list_page.html', context)