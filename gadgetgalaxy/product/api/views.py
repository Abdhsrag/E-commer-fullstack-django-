from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Product
from .serlizer import ProductSerializer

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