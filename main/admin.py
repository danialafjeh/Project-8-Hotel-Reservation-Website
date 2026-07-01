from django.contrib import admin
from .models import HotelInfo, HotelGallery, HotelRoom

# Register your models here.

admin.site.register(HotelInfo)
admin.site.register(HotelGallery)
admin.site.register(HotelRoom)
