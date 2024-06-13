from rest_framework import viewsets, mixins
from api import serializers
from api import models
from drf_spectacular.utils import extend_schema, OpenApiParameter

from api.utils.exception import MyAPIException


@extend_schema(tags=['Suppliers'])
class SupplierViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.inventory.Supplier.objects.all()
    serializer_class = serializers.inventory.SupplierSerializer        

        
@extend_schema(tags=['Items'])
class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.inventory.ItemSerializer
    
    def get_queryset(self):
        supplier_id = self.request.query_params.get('supplier', None)

        if supplier_id:
            try:
                supplier_id = int(supplier_id)
                queryset = models.inventory.Item.objects.filter(suppliers__id=supplier_id).order_by('-date_added')
            except (ValueError, TypeError):
                raise MyAPIException({"detail": "Invalid supplier ID format."})
        else:
            queryset = models.inventory.Item.objects.all().order_by('-date_added')
        return queryset
    
    
    @extend_schema(
        tags=['Items'],
        parameters=[
            OpenApiParameter(
                "supplier",
                type={"type": "integer"},
                location=OpenApiParameter.QUERY,
                description="Filter items by supplier ID"
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
