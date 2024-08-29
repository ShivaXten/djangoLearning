from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('profile')  
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html')

# Login view
def user_login(request):
        return render(request,'login.html')
    
    #  request.method == 'POST':
    #     form = AuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         messages.success(request, 'Login successful.')
    #         return redirect('home')  # Redirect to the home page or any other page
    #     else:
    #         messages.error(request, 'Login failed. Please check your username and password.')
    # else:
    #     form = AuthenticationForm()
    # return render(request, 'login.html')

# Logout view
def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('home')  # Redirect to the home page or any other page

# Profile view (example, requires user to be logged in)
@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
