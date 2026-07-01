from django.db import models
from django.contrib.auth.models import User
from main.models import HotelRoom

# Create your models here.

class Reservation(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, related_name='reservations')
    arrival_date = models.DateField()
    departure_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Room Reservation #{self.id} | User: {self.user.username} | Arrival: {self.arrival_date} - Departure: {self.departure_date}'
