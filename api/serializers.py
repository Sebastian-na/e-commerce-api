from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review, Order, OrderItem, ShippingAddress

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

