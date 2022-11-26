from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate, login
from django.db.models import Sum
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets


from app.models import (Profile, Restaurant, Food_iteams, Order, Transport)

from app.serializers import (Register_Serializers,
                             Login_serializer,
                             Profile_serializer,
                             Restaurant_serializer,
                             Fooditeam_serializer,
                             Order_serializer
                           )

class Pagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class LoginView(APIView):

    serializer_class = Login_serializer

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'})
        login(request, user)
        token, li = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


class Register(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Register_Serializers

class CreateProfileView(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = Profile_serializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class Register_hotel(viewsets.ModelViewSet):

    queryset = Restaurant.objects.all()
    serializer_class = Restaurant_serializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class Foods_from_hotel(viewsets.ModelViewSet):

    queryset = Food_iteams.objects.all()
    serializer_class = Fooditeam_serializer

    def perform_create(self, serializer):
        
        restaurant = Restaurant.objects.get(user = self.request.user)
        serializer.save(hotel = restaurant)

class Order_from_customer(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = Order_serializer

    def perform_create(self, serializer):
        product = Food_iteams.objects.get(id=int(self.request.data['meals']))
        user = Profile.objects.get(user = self.request.user)
        serializer.save(buyer = user, total_price = product.price * int(self.request.data['quantity']))