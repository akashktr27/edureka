from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'profile_list.html')


def about(request):
    return render(request, 'about.html', {'abc': '/about'})

def signup(request):
    if request.method == 'POST':
        username    = request.POST['username']
        firstname   = request.POST['first_name']
        lastname    = request.POST['last_name']
        email       = request.POST['email_id']
        password    = request.POST['password']

        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        x.save()
        print("user created")
        return redirect('/about')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method =='POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        from django.contrib import auth
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('login')
        else:
            return redirect('/')

    else:
        return render(request, 'login.html')


