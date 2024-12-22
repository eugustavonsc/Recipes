from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
class recipeViewsTest(TestCase):
    def test_recipe_home_view_funcion_is_correct(self):
        view= resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    def test_recipe_category_view_funcion_is_correct(self):
        view= resolve(reverse('recipes:category', args=[1]))
        self.assertIs(view.func, views.category)
    def test_recipe_detail_view_funcion_is_correct(self):
        view= resolve(reverse('recipes:recipe', args=[1]))
        self.assertIs(view.func, views.recipe)