from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__' # Para que se serialicen todos los campos