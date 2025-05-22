from unicodedata import category

from rest_framework import serializers
from ..models import Product
from category.models import Category

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
    date_added = serializers.DateTimeField(read_only=True)
    is_deleted = serializers.BooleanField(default=False)
    image = serializers.ImageField()
    sku = serializers.CharField(max_length=50)
    category_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        try:
            category = Category.objects.get(id=category_id)
            product = Product.objects.create(category=category, **validated_data)
            return product
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this ID does not exist.")

    def update(self, instance, validated_data):
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            try:
                category = Category.objects.get(id=category_id)
                instance.category = category
            except Category.DoesNotExist:
                raise serializers.ValidationError("Category with this ID does not exist.")

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.image = validated_data.get('image', instance.image)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance
