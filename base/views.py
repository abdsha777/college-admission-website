from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from base.models import User

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def loginPage(request):
    if request.method=="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Password is Invalid')

    context={'page':'login'}
    return render(request,'base/login_signup.html',context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Input')
    form = UserCreationForm()
    context={'form':form}
    for field in form:
        print(field.label)
    return render(request,'base/login_signup.html',context)