from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'article']
    filterset_fields = ['status']
