from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate
from .models import CarMake, CarModel


# Get an instance of a logger
logger = logging.getLogger(__name__)

def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})
    return JsonResponse({"CarModels":cars})

# TEST VIEW - This will show us what's wrong
def test_auth(request):
    html = "<h1>Authentication Test</h1>"
    
    # Show all users
    html += "<h2>All Users in Database:</h2>"
    users = User.objects.all()
    for user in users:
        html += f"<p>Username: {user.username} | Staff: {user.is_staff} | Superuser: {user.is_superuser} | Active: {user.is_active}</p>"
    
    # Test manual authentication
    html += "<h2>Testing Manual Authentication:</h2>"
    try:
        user = authenticate(username='root', password='root')
        if user:
            html += f"<p style='color:green'>✓ Authentication SUCCESS for root/root</p>"
            html += f"<p>User: {user.username} | Staff: {user.is_staff} | Superuser: {user.is_superuser}</p>"
        else:
            html += f"<p style='color:red'>✗ Authentication FAILED for root/root</p>"
    except Exception as e:
        html += f"<p style='color:red'>Error during authentication: {e}</p>"
    
    # Show current user
    html += "<h2>Current Request User:</h2>"
    if request.user.is_authenticated:
        html += f"<p style='color:green'>Current user: {request.user.username}</p>"
    else:
        html += f"<p style='color:orange'>No user currently logged in</p>"
    
    # Manual login test
    html += "<h2>Manual Login Test:</h2>"
    html += '''
    <form method="post">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Test Login">
    </form>
    '''
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            html += f"<p style='color:green'>✓ LOGIN SUCCESS for {username}</p>"
            html += f"<p>Now try admin: <a href='/admin/'>Go to Admin</a></p>"
        else:
            html += f"<p style='color:red'>✗ LOGIN FAILED for {username}/{password}</p>"
    
    return HttpResponse(html)