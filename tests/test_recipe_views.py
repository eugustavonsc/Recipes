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
    
    def test_recipe_home_view_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_uses_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn( 'No recipes found here :( ', response.content.decode("utf-8"))