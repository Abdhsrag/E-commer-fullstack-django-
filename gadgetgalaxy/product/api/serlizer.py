from rest_framework import serializers
from gadgetgalaxy.product.models import Product
from gadgetgalaxy.category.models import Category

class CatagorySerlizer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields='__all__'

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        try:
            category = Category.objects.get(id=category_id)
            product = Product.objects.create(category=category, **validated_data)
            return product
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this ID does not exist.")