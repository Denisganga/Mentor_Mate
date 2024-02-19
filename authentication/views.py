from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
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

        return redirect('authentication:homepage')
    
    return render(request,'register.html')


def Homepage(request):
    #profiles=Profile.objects.all()
    return render(request, 'homepage.html')

def Show_profile(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request,'profile.html')

@login_required
def edit_profile(request):
    try:
        profile=Profile.objects.get(user=request.user)
        
    except Profile.DoesNotExist:
        profile=None
        
    form=ProfileForm(instance=profile)

    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('authentication:profile')
        else:
            form=ProfileForm(instance=profile)
            
    return render(request, 'editprofile.html',{'form':form})
            
            
        



