from django.shortcuts import render, get_object_or_404
from .models import HotelGallery, HotelInfo, HotelRoom

# Create your views here.

def home(request):
    sale_rooms = HotelRoom.objects.filter(is_sale=True)
    gallery_ids = [1,2,3,8]
    gallery_images = HotelGallery.objects.filter(id__in=gallery_ids)
    info = {
        'gallery':gallery_images, 
        'rooms':sale_rooms
    }
    return render(request, 'home.html', info)

def gallery(request):
    gallery_images = HotelGallery.objects.all()
    info = {'gallery':gallery_images}
    return render(request, 'gallery.html', info)

def about(request):
    hotel_info = get_object_or_404(HotelInfo, id=1)
    info = {'information':hotel_info}
    return render(request, 'about.html', info)

def rooms(request):
    all_rooms = HotelRoom.objects.all()
    info = {'rooms':all_rooms}
    return render(request, 'rooms.html', info)


