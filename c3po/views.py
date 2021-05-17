from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import serializers
from .models import Student


def students_form(request):

    return render(request,'student.html')

def student_submit(request):
    print("form submitted")
    s_id = request.POST['s_id']
    s_name = request.POST['s_name']
    s_email = request.POST['s_email']
    s_address = request.POST['s_address']
    x = Student(s_id=s_id, s_name=s_name, s_email=s_email, s_address=s_address)
    x.save()
    return render(request, 'student.html')

def nav(request):
    return render(request,'navbar.html')





