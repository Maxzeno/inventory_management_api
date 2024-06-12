from rest_framework import serializers
from api import models
from api.utils.exception import MyAPIException


class SupplierSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    contact_information = serializers.CharField(required=False)
    class Meta:
        model = models.inventory.Supplier
        fields = ['id', 'name', 'contact_information']
        
    def validate(self, attrs):
        print('validate', attrs)
        
        if not attrs.get('name'):
            raise MyAPIException(detail="Name is required", code=400)
        
        if not attrs.get('contact_information'):
            raise MyAPIException(detail="Contact information is required", code=400)
        
        return attrs


class SupplierIDsField(serializers.ListField):
    child = serializers.IntegerField()

    def to_representation(self, value):
        return [supplier.id for supplier in value]

    def to_internal_value(self, data):
        try:
            return [models.inventory.Supplier.objects.get(id=id) for id in data]
        except models.inventory.Supplier.DoesNotExist:
            raise MyAPIException(detail="Supplier not found", code=404)


class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    
    suppliers = SupplierSerializer(many=True, read_only=True)
    supplier_ids = SupplierIDsField(write_only=True)

    class Meta:
        model = models.inventory.Item
        fields = ['id', 'name', 'description', 'price', 'date_added', 'suppliers', 'supplier_ids']
        extra_kwargs = {
            'suppliers': {'read_only': True},
        }
        
        
    def validate(self, attrs):
        print('validate', attrs)
        
        if not attrs.get('name'):
            raise MyAPIException(detail="Name is required", code=400)
        
        if not attrs.get('description'):
            raise MyAPIException(detail="Description is required", code=400)
        
        if not attrs.get('price'):
            raise MyAPIException(detail="Price is required", code=400)
        
        return attrs

    def create(self, validated_data):
        supplier_ids = validated_data.pop('supplier_ids', [])
        item = models.inventory.Item.objects.create(**validated_data)
        item.suppliers.set(supplier_ids)
        return item

    def update(self, instance, validated_data):
        supplier_ids = validated_data.pop('supplier_ids', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if supplier_ids is not None:
            instance.suppliers.set(supplier_ids)
        instance.save()
        return instance
