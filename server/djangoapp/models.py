from django.db import models
from django.utils.timezone import now

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # Add any other fields you need for a car make

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as needed
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=CAR_TYPES)
    year = models.DateField()
    # Add any other fields you need for a car model

    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year.year}) {self.type}"


# Plain Python class for CarDealer
class CarDealer:
    def __init__(self, dealer_id, name, city, state):
        self.dealer_id = dealer_id
        self.name = name
        self.city = city
        self.state = state


# Plain Python class for DealerReview
class DealerReview:
    def __init__(self, review_id, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year):
        self.review_id = review_id
        self.name = name
        self.dealership = dealership
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
