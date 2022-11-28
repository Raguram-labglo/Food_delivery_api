from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='user_profile', blank=False)
    contact_no = models.PositiveIntegerField()
    address= models.TextField()
    alternate_address = models.TextField(null = True)
    

    def __str__(self):
        return '{}'.format(self.user)

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    address = models.TextField(max_length=200)
    logo = models.ImageField(upload_to='restaurant_logo', blank=False)

    def __str__(self):
        return self.name

class Food_iteams(models.Model):
    hotel = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food = models.CharField(max_length= 200)
    image = models.ImageField(upload_to='foods')
    price = models.IntegerField()
    available = models.BooleanField()

    def __str__(self):
        return '{}, {}'.format(self.hotel, self.food)

class Order(models.Model):
    cooking = 0
    on_the_way = 1
    delivery = 2
    cancel = 3
    delivered = 4

    order = [(0, 'waiting'),
            (1, 'cooking'), 
            (2, 'on_the_way'),
            (3, 'cancel'),
            (4, 'delivered')
            ]
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meals = models.ManyToManyField(Food_iteams)
    # quantity = models.IntegerField()
    total_price = models.IntegerField()
    order_status = models.IntegerField(choices=order, default=0)

    def __str__(self):
        return '{}' .format(self.buyer)

