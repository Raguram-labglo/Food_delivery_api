from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('profile_register', UserRegister, basename='User')
router.register('register_hotels', Register_hotel)
router.register('add_foods', Foods_from_hotel)
router.register('order', Order_from_customer, basename= 'customer')
router.register('foods', Food_list, basename='Menu')
router.register('hotel_orders', Order_status, basename= 'Hotel')
urlpatterns = [
                path('login', LoginView.as_view()),
               ]+router.urls