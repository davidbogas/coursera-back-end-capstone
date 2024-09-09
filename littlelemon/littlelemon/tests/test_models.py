from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_menu(self):
        menu = Menu.objects.create(title='Chicken Tikka Masala', price=10.0, inventory=7)
        itemstr = menu.__str__()

        self.assertEqual(itemstr, 'Chicken Tikka Masala : 10.0')