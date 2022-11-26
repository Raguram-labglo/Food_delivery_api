from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('register', Register)
router.register('profile', CreateProfileView)
router.register('register_hotels', Register_hotel)
router.register('foods', Foods_from_hotel)
router.register('order', Order_from_customer)

urlpatterns = [
                path('login', LoginView.as_view()),
               ]+router.urls