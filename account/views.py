from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from reservation.models import Reservation
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm

# Create your views here.

def profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        user_reservations = Reservation.objects.filter(user=user)
        info = {'user_info':user, 'reservations':user_reservations}
        return render(request, 'profile.html', info)
    else:
        messages.error(request, ('Sorry, You must be signed in to an account first.'))
        return redirect('home_page')
    
def signin_choice(request):
    return render(request, 'signin_choice.html')

def signin_guests(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.is_staff:
                login(request, user)
                messages.success(request, ('You are now signed in to your account.'))
                return redirect('home_page')
            else:
                messages.error(request, ('Sorry, This is an admin account.'))
                return redirect('signin_guests_page')
        else:
            messages.error(request, ('Sorry, There is no account with these info.'))
            return redirect('signin_guests_page')
    else:
        return render(request, 'signin_guests.html')
    
def signin_admins(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                messages.success(request, ('You are now signed in to your account.'))
                return redirect('home_page')
            else:
                messages.error(request, ('Sorry, This is a guest account.'))
                return redirect('signin_admins_page')
        else:
            messages.error(request, ('Sorry, There is no account with these info.'))
            return redirect('signin_admins_page')
    else:
        return render(request, 'signin_admins.html')
    
def signout_account(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, ('You are signed out of your account.'))
        return redirect('home_page')
    else:
        messages.error(request, ('Sorry, You must be signed in to an account first.'))
        return redirect('home_page')
    
def signup_account(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your account has been created.'))
            return redirect('signin_choice_page')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

            return redirect('signup_page')
    else:
        return render(request, 'signup.html', {'form':form})
    
def update_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        form = UpdateUserForm(instance=user)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, ('Your profile has been updated.'))
                return redirect('profile_page')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)

                return redirect('update_profile_page')
        else:
            return render(request, 'update_profile.html', {'form':form})
    else:
        messages.error(request, ('Sorry, You are not allowed to perform this action.'))
        return redirect('home_page')
    
def update_password(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdatePasswordForm(user)
        if request.method == 'POST':
            form = UpdatePasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ('Your password has been changed. Sign in again.'))
                logout(request)
                return redirect('signin_choice_page')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)

                return redirect('update_password_page')
        else:
            return render(request, 'update_password.html', {'form':form})
    else:
        messages.error(request, ('Sorry. You are not allowed to perform this action'))
        return redirect('home_page')
            