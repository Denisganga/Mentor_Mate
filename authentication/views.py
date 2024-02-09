from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

def Register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmPassword=request.POST.get('confirmPassword')

            #checking if the passwords match
        if password != confirmPassword:
            error_message="Passwords do not match"
            return render(request, 'register.html',{'error_message':error_message})
        
        #checking if the username exists

        if User.objects.filter (username=username).exists():
            error_message="The user already exists. Use another username"
            return render (request, 'register.html', {'error_message':error_message})
     
        #checking if the email exists

        if User.objects.filter(email=email).exists():
            error_message="The email address is registered under an account"
            return render(request, 'register.html',{'error_message':error_message})
        
        #creating a new user
        new_user= User.objects.create_user(username=username, email=email, password=password)
        new_user.save()

        messages.success(request,"An account was successfully registered")
    
    return render(request,'register.html')


