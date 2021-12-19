from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review, Order, OrderItem, ShippingAddress
from rest_framework_simplejwt.tokens import RefreshToken

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    _id = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', '_id' 'username', 'email', 'name', 'is_admin']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name =  obj.email
        return name

    def get__id(self, obj):
        return obj.id

    def get_is_admin(self, obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', '_id' 'username', 'email', 'name', 'is_admin', 'token']
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

