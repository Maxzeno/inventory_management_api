from rest_framework import serializers
from api import models 

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.inventory.Supplier
        fields = ['id', 'name', 'contact_information', 'items']

class ItemSerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)

    class Meta:
        model = models.inventory.Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers']
