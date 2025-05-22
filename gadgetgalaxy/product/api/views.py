from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers
from ..models import Product
from category.models import Category
from .serlizer import ProductSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet



@api_view(['GET', 'POST'])
def product_list_api(request):
    if request.method == 'GET':
        products = Product.objects.filter(is_deleted=False)
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={ 'msg': 'product created'+ str(serializer.data['id'])},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data={'msg': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'msg': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Product updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductGetIdUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        category_id = self.request.data.get('category_id')
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                serializer.save(category=category)
                return
            except Category.DoesNotExist:
                raise serializers.ValidationError("Category with this ID does not exist.")

        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'msg': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_deleted=False)
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        category_id = self.request.data.get('category_id')
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                serializer.save(category=category)
            except Category.DoesNotExist:
                raise serializers.ValidationError("Category with this ID does not exist.")
        else:
            serializer.save()

    def perform_update(self, serializer):
        category_id = self.request.data.get('category_id')
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                serializer.save(category=category)
            except Category.DoesNotExist:
                raise serializers.ValidationError("Category with this ID does not exist.")
        else:
            serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'msg': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)