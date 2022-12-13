from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'article', 'cost', 'status', 'image')
        model = Product
