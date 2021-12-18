from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .products import products
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response({"data": "Hello World"})

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
