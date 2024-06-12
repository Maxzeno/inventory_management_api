from django_filters import rest_framework as filters

class ItemFilter(filters.FilterSet):
    suppliers = filters.NumberFilter()