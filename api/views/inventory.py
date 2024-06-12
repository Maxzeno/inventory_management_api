from rest_framework import viewsets
from api import serializers
from api import models
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend

from api.utils.exception import MyAPIException
from api.utils.filters import ItemFilter


@extend_schema(tags=['Suppliers'])
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.inventory.Supplier.objects.all()
    serializer_class = serializers.inventory.SupplierSerializer        

        
@extend_schema(tags=['Items'])
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.inventory.ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilter
    
    def get_queryset(self):
        supplier_id = self.request.query_params.get('suppliers', None)

        if supplier_id:
            try:
                supplier_id = int(supplier_id)
                queryset = models.inventory.Item.objects.filter(suppliers__id=supplier_id).order_by('-date_added')
            except (ValueError, TypeError):
                raise MyAPIException({"detail": "Invalid supplier ID format."})
        else:
            queryset = models.inventory.Item.objects.all().order_by('-date_added')
        return queryset
