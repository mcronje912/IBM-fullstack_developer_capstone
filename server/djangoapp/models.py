from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=100, default='')
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    # Dealer ID from Cloudant database
    dealer_id = models.IntegerField()
    name = models.CharField(null=False, max_length=100, default='')

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('COUPE', 'Coupe'),
        ('PICKUP', 'Pickup'),
    ]
    type = models.CharField(
        null=False, max_length=50, choices=CAR_TYPES, default='SUV')
    year = models.DateField()

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
