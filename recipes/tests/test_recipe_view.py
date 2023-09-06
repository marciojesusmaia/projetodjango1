from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User


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

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(first_name='user', last_name='name', username='username', password='123456', email='username@email.com')
        recipe = Recipe.objects.create(category=category, author=author,title='Recipe Title', description='receita teste', 
                                        slug='slug-teste', preparation_time=10, preparation_time_unit='minuto', servings=8,
                                        servings_unit='pedacinho', preparatio_steps='step', preparatio_steps_is_html=False, 
                                        is_published=True, )
        assert 1 == 1

    def test_recipe_home_loads_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/partial/footer.html')

    def test_category_home_return_status_404_is_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id':1,}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_home_return_status_404_is_not_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id':1}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_show_no_recipes_found_if_no_recipe(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('Sem receitas ainda', response.content.decode('utf-8'))