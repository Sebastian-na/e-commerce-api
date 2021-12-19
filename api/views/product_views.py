from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Product
from ..serializers import ProductSerializer


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    data = ProductSerializer(product).data
    return Response(data)