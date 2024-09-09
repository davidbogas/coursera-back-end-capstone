from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title='Chicken Tikka Masala', price=10.0, inventory=7)
        self.menu2 = Menu.objects.create(title='Spaghetti Bolognese', price=8.0, inventory=8)
        self.menu3 = Menu.objects.create(title='Boneless Chicken', price=5.0, inventory=10)

        self.client = APIClient()

        self.user = User.objects.create_user(username = 'Customer1', password='coursera@123!')
        self.token = Token.objects.create(user = self.user)
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

    def test_menu(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
