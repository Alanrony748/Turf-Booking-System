from django.db import models

# Create your models here.

class TurfDb(models.Model):
    turf_name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    sport_type=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    available=models.BooleanField(default=True)

    def __str__(self):
        return self.turf_name

class BookingDb(models.Model):
    customer_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    turf_id=models.IntegerField()
    No_players=models.IntegerField(null=True)
    booking_date=models.DateField()
    start_time=models.TimeField(null=True,blank=True)

    def __str__(self):
        return self.customer_name