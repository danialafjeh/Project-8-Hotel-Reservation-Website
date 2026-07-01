from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('gallery/', views.gallery, name='gallery_page'),
    path('about/', views.about, name='about_page'),
    path('rooms/', views.rooms, name='rooms_page')
]
