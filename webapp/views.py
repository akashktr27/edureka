from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import serializers
from .serializers import EmployeeSerializer
from .models import Employees
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import Login_forms
from rest_framework import viewsets
# Create your views here.



@csrf_exempt
def employeelist(request):
    if request.method == 'GET':
        articles = Employees.objects.all()
        serializer = EmployeeSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

def homepage(request):
    return render(request, 'home.html',{ 'title': 'Home','cname': 'success'})

def nav(request):
    return render(request, 'testing_nav.html')


def bootstrap(request):
    return render(request, 'check_bootstrap.html')

def signin(request):
    return render(request, 'index.html')


def register(request):
     if request.method == 'POST':
         username = request.POST['username']
         firstname = request.POST['first_name']
         lastname   = request.POST['last_name']
         email      = request.POST['email_id']
         password   = request.POST['password']

         x =User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
         x.save()
         print("user created")
     else:
         return render(request,'register.html')


    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    # # context = {'form': form}
    # return render(request, 'register.html')


# def Loginregister(request):
#     form = Login_forms
#
#     if request.method == 'POST':
#         form = Login_forms(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {'form': form}
#     return render(request, 'register.html', context)


