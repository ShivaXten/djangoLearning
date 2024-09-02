from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
#this is from the rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer


# This is to register the new user and also direct it to create_profile  (POST)
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            Profile.objects.create(user=user)  # Create a profile for the user
            auth_login(request, user)
            return redirect('create_profile')  # Redirect to the profile creation page
    else:
        user_form = UserRegisterForm()
    return render(request, 'registration.html', {'form': user_form})



# This is to login the existing  user from the database by checking the username and password field (POST)
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.POST.get('next', 'dashboard')  # Redirect to 'next' or 'dashboard'
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    next_url = request.GET.get('next', 'register')  # Default to 'register' if no 'next'
    return render(request, 'login.html', {'form': form, 'next': next_url})



# This is to logout the existing credentials  
def logout(request):
    auth_logout(request)
    return redirect('login')



# This is to show the dashboard only if the user is valid in the database decorator login is used 
@login_required
def dashboard(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'dashboard.html', {'profile': profile})



# This is to create the user profile and save in the database as Profile form will pass files too that is image (POST) 
# if created it will redirect directly to dashboard
def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')  
    else:
        profile_form = ProfileForm()
    return render(request, 'create_profile.html', {'profile_form': profile_form})



# This is to update the user profile only it uses rest_framework decorators 
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)