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
from .permissions import IshotelOrReadOnly, User_can_see_order, Hotel_waiting_orders
from rest_framework.permissions import IsAuthenticated

from app.models import (Profile, Restaurant, Food_iteams, Order)

from app.serializers import (Register_Serializers,
                             Login_serializer,
                             Profile_serializer,
                             Restaurant_serializer,
                             Fooditeam_serializer,
                             Order_serializer,
                             Hotel_register,
                             Orders_condition)

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


class UserRegister(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Register_Serializers
    http_method_names = ['post']


class Register_hotel(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = Hotel_register
    http_method_names = ['post']


    # def get_queryset(self):
    #     return Restaurant.objects.filter(user = self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)

class Foods_from_hotel(viewsets.ModelViewSet):

    queryset = Food_iteams.objects.all()
    serializer_class = Fooditeam_serializer
    permission_classes = [IshotelOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        user = Restaurant.objects.get(user = self.request.user)
        
        return Food_iteams.objects.filter(hotel = user)

    def perform_create(self, serializer):
        
        restaurant = Restaurant.objects.get(user = self.request.user)
        serializer.save(hotel = restaurant)


class Food_list(viewsets.ModelViewSet):
    queryset = Food_iteams.objects.all()
    serializer_class = Fooditeam_serializer
    pagination_class = Pagination
    http_method_names = ['get']
    

class Order_from_customer(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = Order_serializer
    permission_classes = [User_can_see_order, IsAuthenticated]

    def get_queryset(self):
        user = Profile.objects.get(user = self.request.user)
        return Order.objects.filter(buyer = user)

    def perform_create(self, serializer):
        print(self.request.data)
        product = dict(self.request.data)
        pro = product['meals']
        pr = []
        restaruent = []
        for ids in pro:
            foods = Food_iteams.objects.get(id = ids)
            pr.append(foods.price)
            restaruent.append(foods.hotel)
    
        total = sum(pr)
        user = Profile.objects.get(user = self.request.user)
        res = Food_iteams.objects.get(id = self.request.data['meals'])
        serializer.save(buyer = user, total_price = total, restaurant = res.hotel)


class Order_status(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = Orders_condition
    permission_classes = [IsAuthenticated]
   # parser_classes = [Hotel_waiting_orders]
    def get_queryset(self):
        res = Restaurant.objects.get(user = self.request.user)
        return Order.objects.filter(restaurant = res)
        