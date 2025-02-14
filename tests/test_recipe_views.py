from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

class recipeViewsTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        # Testa se a função da view da página inicial está correta
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        # Testa se a view da página inicial retorna o status code 200 (OK)
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        # Testa se a view da página inicial carrega o template correto
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Testa se a mensagem "No recipes found here :(" é exibida quando não há receitas
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here :( </h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        # Testa se as receitas são carregadas no template da página inicial
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)
    
    def test_recipe_home_template_dont_load_recipes_not_published(self):
        # Testa se as receitas são carregadas no template da página inicial
        self.make_recipe( is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here :( </h1>',
            response.content.decode('utf-8')
        )


    def test_recipe_category_view_function_is_correct(self):
        # Testa se a função da view da página de categoria está correta
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)
    
    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        # Testa se a view da página de categoria retorna 404 quando não há receitas
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_category_template_loads_recipes(self):
        # Testa se as receitas são carregadas no template da página de categoria
        needed_title = 'this is a category test'
        self.make_recipe( title=needed_title)
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
        
        self.assertIn(needed_title, content)
    
    def test_recipe_category_template_dont_load_recipes_not_published(self):
        # Testa se as receitas são carregadas no template da página inicial
        recipe= self.make_recipe( is_published=False)
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )        
        self.assertEqual(response.status_code, 404)
        

    def test_recipe_detail_view_function_is_correct(self):
        # Testa se a função da view da página de detalhes da receita está correta
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        # Testa se a view da página de detalhes da receita retorna 404 quando não há receitas
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_detail_template_loads_the_correct_recipe(self):
        # Testa se o template da página de detalhes da receita carrega a receita correta
        needed_title = 'This is a detail page - It load one recipe'
        # Cria uma receita
        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': 1
                }
            )
        )
        content = response.content.decode('utf-8')
        # checa se o título da receita está no conteúdo da página
        self.assertIn(needed_title, content)
    
    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        # Testa se as receitas são carregadas no template da página inicial
        recipe= self.make_recipe( is_published=False)
        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={
                    'id': recipe.category.id
                }
            )
        ) 
        self.assertEqual(response.status_code, 404)
