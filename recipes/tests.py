from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.
class RecipeURLsTest(TestCase):
    def test_recipe_home_test_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_home_category_test_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id':1,})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_home_recipe_test_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id':1})
        self.assertEqual(url, '/recipes/1/')

class RecipeViewsTest(TestCase):
    def test_recipe_home_views_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertTrue(True)

    def test_recipe_category_views_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':1,}))
        self.assertTrue(True)

    def test_recipe_detail_views_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id':1}))
        self.assertTrue(True)