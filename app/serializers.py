from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import (Profile, Restaurant, Food_iteams, Order, Transport)

class Register_Serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create_superuser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class Login_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class Profile_serializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user',)

class Restaurant_serializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ['id', 'user', 'name', 'phone' , 'address' , 'logo']
        read_only_fields = ('user',)

class Fooditeam_serializer(serializers.ModelSerializer):
    
    hotel = Restaurant_serializer(read_only = True)
    class Meta:
        model = Food_iteams
        fields = ['id', 'hotel', 'food', 'image', 'price', 'available']
        read_only_fields = ('hotel',)

class Order_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['buyer', 'meals', 'quantity', 'total_price', 'order_status']
        read_only_fields = ('total_price', 'buyer', 'order_status')
