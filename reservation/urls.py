from django.urls import path
from . import views

urlpatterns = [
    path('book_room/<int:pk>', views.reservation_page, name='reservation_page'),
    path('checkout/', views.reservation_checkout, name='reservation_checkout'),
    path('cancel/<int:pk>', views.reservation_cancel, name='reservation_cancel')
]
