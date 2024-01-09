from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render, redirect

def home(request):
    return render(request,"category.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.info(request, "Please fill all the fields")
            return render(request, "login.html")

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,"category.html")
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if username and password:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Already exists")
                else:
                    user = User.objects.create_user(username=username, password=password,email=email)
                    user.save()
                    return render(request,"category.html")
            else:
                messages.info(request, "Passwords do not match")
        else:
            messages.info(request, "Username and password fields cannot be empty")

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return render(request, "category.html")
