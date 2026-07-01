from django.db import models

# Create your models here.

class HotelInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    phone_1 = models.CharField(max_length=30)
    phone_2 = models.CharField(max_length=30, blank=True, null=True)
    phone_3 = models.CharField(max_length=30, blank=True, null=True)
    email_1 = models.EmailField()
    email_2 = models.EmailField(blank=True, null=True)
    email_3 = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Hotel Info'

    def __str__(self):
        return f'Hotel Primary Information'

    
class HotelGallery(models.Model):
    section = models.CharField(max_length=250)
    image = models.ImageField(upload_to='upload/gallery')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Hotel Gallery'

    def __str__(self):
        return f'Hotel Gallery - Section {self.section}'
    
class HotelRoom(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to='upload/rooms')
    guests_capacity = models.PositiveIntegerField(default=1)
    beds = models.CharField(max_length=150)
    price_per_night = models.DecimalField(max_digits=10, default=0, decimal_places=0)
    is_sale = models.BooleanField(default=False)
    sale_price_per_night = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_in_service = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Hotel Room - Number {self.room_number}'




