from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from api import models

class InventoryTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = models.user.User.objects.create_user(email='testuser@test.com', username='testuser', password='testpassword')
        models.user.EmployeeProfile.objects.create(user=self.user)
        
        # Obtain token
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Set up the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_create_item(self):
        supplier = models.inventory.Supplier.objects.create(name="Supplier1", contact_information="Contact info")
        response = self.client.post('/api/v1/items/', {
            'name': 'Item1',
            'description': 'Item description',
            'price': '9.99',
            'supplier_ids': [supplier.id]
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_supplier(self):
        response = self.client.post('/api/v1/suppliers/', {
            'name': 'Supplier1',
            'contact_information': 'Contact info'
        }, format='json')
        
        self.assertEqual(response.status_code, 201)
