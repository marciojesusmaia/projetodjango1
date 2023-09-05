from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertTrue(view.func, views.home)

    def test_recipe_category_views_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':1,}))
        self.assertTrue(view.func, views.category)

    def test_recipe_detail_views_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id':1}))
        self.assertTrue(view.func, views.recipe)

    def test_recipe_home_return_status_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/partial/footer.html')

    def test_recipe_home_show_no_recipes_found_if_no_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Sem receitas ainda', response.content.decode('utf-8'))