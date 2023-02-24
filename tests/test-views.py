from django.test import TestCase, RequestFactory
from restaurant.views import *
from restaurant.models import Menu
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        Menu.objects.create(Title='Pasta', Price=50, Inventory=200)
        Menu.objects.create(Title='Greek Salad', Price=20, Inventory=300)
    
    def test_getall(self):
        self.setUp()

        factory = RequestFactory()
        # Create an instance of a GET request.
        request = factory.get('/restaurant/menu/items/')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        #request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        #response = my_view(request)

        # Use this syntax for class-based views.
        response = MenuItemsView.as_view()(request)
        
        serializedData = MenuSerializer(data=response, many=True)    

        self.assertEqual(response.status_code, 200)
        