from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile_page'),
    path('signin/', views.signin_choice, name='signin_choice_page'),
    path('signin_guests/', views.signin_guests, name='signin_guests_page'),
    path('signin_admins/', views.signin_admins, name='signin_admins_page'),
    path('signout/', views.signout_account, name='signout_account'),
    path('signup/', views.signup_account, name='signup_page'),
    path('update_profile/', views.update_profile, name='update_profile_page'),
    path('update_password/', views.update_password, name='update_password_page')
]