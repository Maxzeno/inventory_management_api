from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from api import models


class InventoryTests(APITestCase):
    def setUp(self):
        self.user = models.user.User.objects.create_user(email='testuser@test.com', username='testuser', password='testpassword')
        models.user.EmployeeProfile.objects.create(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_item(self):
        supplier = models.inventory.Supplier.objects.create(name="Supplier1", contact_information="Contact info")
        response = self.client.post('/api/v1/items/', {
            'name': 'Item1',
            'description': 'Item description',
            'price': '9.99',
            'supplier_ids': [str(supplier.id)]
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_supplier(self):
        response = self.client.post('/api/v1/suppliers/', {
            'name': 'Supplier1',
            'contact_information': 'Contact info'
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_item(self):
        supplier = models.inventory.Supplier.objects.create(name="Supplier1", contact_information="Contact info")
        item = models.inventory.Item.objects.create(name="Item1", description="Item description", price=9.99)
        item.suppliers.add(supplier)
        response = self.client.get(f'/api/v1/items/{item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Item1")
        self.assertEqual(response.data['suppliers'][0]['name'], "Supplier1")

    def test_get_supplier(self):
        supplier = models.inventory.Supplier.objects.create(name="Supplier1", contact_information="Contact info")
        response = self.client.get(f'/api/v1/suppliers/{supplier.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "Supplier1")
