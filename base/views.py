from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm 
from .forms import MyUserCreationForm
from django.contrib import messages
from base.models import User

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def loginPage(request):
    if request.method=="POST":
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        try:
            user = User.objects.get(mobile=mobile)
            user = authenticate(request,mobile=mobile,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Password is Invalid')
        except:
            messages.error(request,"User does not exist")
        

    context={'page':'login'}
    return render(request,'base/login_signup.html',context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    if request.method=='POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Input')
    form = MyUserCreationForm()
    context={'form':form}
    for field in form:
        print(field.label)
    return render(request,'base/login_signup.html',context)