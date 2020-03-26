import django
from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Category, MenuItem


class CategoryTestCase(TestCase):
    def test_create(self):
        Category.objects.create(name="Drinks")


class MenuItemTestCase(TestCase):
    def test_create(self):
        cat = Category.objects.create(name="Drinks")
        MenuItem.objects.create(
            name="Coke",
            item_id='D1',
            category=cat,
            description='Gassy cough medicine.',
            thumbnail='https://picsum.photos/id/237/200/300')

    def test_create_missing_category(self):
        with self.assertRaises(django.db.utils.IntegrityError,
                               msg='Should require category.'):
            MenuItem.objects.create(
                name="Coke",
                item_id='D1',
                description='Gassy cough medicine.',
                thumbnail='https://picsum.photos/id/237/200/300')

    def test_str(self):
        cat = Category.objects.create(name="Drinks")
        item = MenuItem.objects.create(
            name="Coke",
            item_id='D1',
            category=cat,
            description='Gassy cough medicine.',
            thumbnail='https://picsum.photos/id/237/200/300')
        self.assertEqual(str(item), 'D1 - Coke')


class URLsTest(TestCase):
    def setUp(self):
        User.objects.create_user('john',
                                 'lennon@thebeatles.com',
                                 'johnpassword',
                                 is_staff=True)
        drinks = Category.objects.create(name="Drinks")
        sushi = Category.objects.create(name="Sushi")
        MenuItem.objects.create(
            name="Coke",
            item_id='D1',
            category=drinks,
            description='Gassy cough medicine.',
            thumbnail='https://picsum.photos/id/237/200/300')
        MenuItem.objects.create(
            name="Salmon Sushi",
            item_id='S1',
            category=sushi,
            description='Swam up to river to you.',
            thumbnail='https://picsum.photos/id/236/200/300')

    def test_admin(self):
        client = Client()
        response = client.get('/admin/')
        self.assertEqual(response.status_code, 302)

    def test_menu_get(self):
        client = Client()
        response = client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(
            response.json()[0], {
                'name': 'Coke',
                'item_id': 'D1',
                'category': 'Drinks',
                'description': 'Gassy cough medicine.',
                'thumbnail': 'https://picsum.photos/id/237/200/300'
            })

    def test_menu_get_limit_query(self):
        client = Client()
        response = client.get('/menu/?limit=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1, 'Should return only 1 item')

    def test_menu_get_NaN_limit_query(self):
        client = Client()
        response = client.get('/menu/?limit=a')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['detail'], 'Limit must be a number.')

    def test_menu_get_category(self):
        client = Client()
        response = client.get('/menu/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(
            response.json()[0], {
                'name': "Salmon Sushi",
                'item_id': 'S1',
                'category': 'Sushi',
                'description': 'Swam up to river to you.',
                'thumbnail': 'https://picsum.photos/id/236/200/300'
            })

    def test_item_post(self):
        client = Client()
        client.login(username='john', password='johnpassword')
        response = client.post(
            '/item/4/', {
                'name': "Beef Sushi",
                'item_id': 'S2',
                'category': 2,
                'description': 'Amoozing.',
                'thumbnail': 'https://picsum.photos/id/235/200/300'
            })
        self.assertEqual(response.status_code, 200)
        item = MenuItem.objects.get(pk=4)
        self.assertEqual(item.name, 'Beef Sushi')

    def test_item_delete(self):
        client = Client()
        client.login(username='john', password='johnpassword')
        response = client.delete('/item/2/')
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(MenuItem.DoesNotExist):
            MenuItem.objects.get(pk=2)

    def test_category_post(self):
        client = Client()
        client.login(username='john', password='johnpassword')
        response = client.post('/category/', {
            'name': "Bento",
        })
        self.assertEqual(response.status_code, 201)
        cat = Category.objects.get(name='Bento')
        self.assertEqual(cat.name, 'Bento')