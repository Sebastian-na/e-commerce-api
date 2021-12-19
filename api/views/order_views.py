from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from api.models import Order, OrderItem, Product, ShippingAddress
from api.serializers import ProductSerializer

from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user = request.user
    data = request.data
    orderItems = data['orderItems']

    if orderItems and len(orderItems) == 0:
        return Response({"detail": "No order items found"}, status=status.HTTP_400_BAD_REQUEST)
    


    return Response('Order')