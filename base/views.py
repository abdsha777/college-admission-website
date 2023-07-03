from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm 
from .forms import MyUserCreationForm,ApplicationForm
from django.contrib import messages
from base.models import User,Application
# from django.views import View
# from django.utils.decorators import method_decorator
from datetime import date


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


@login_required(login_url='login')
def fillFormPage(request):
    if request.POST.get('option')=='next1':
        application = Application.objects.filter(user=request.user, className=request.POST.get('classList')).first()
        if application:
            # messages.error(request,"You already have an existing form for that class")
            # return redirect('home')
            pass
        else:
            application = Application(user=request.user,className=request.POST.get('classList'))
            application.status = 'pending'
            application.save()
        return redirect('form',pk=application.pk)
    elif request.method == 'POST':
        selected_option = request.POST.get('option')
        if selected_option == 'undergraduate':
            class_list = ['F.Y.B.C.A.', 'S.Y.B.C.A.']  # Example list for undergraduate
        elif selected_option == 'postgraduate':
            class_list = ['F.Y.M.C.A.', 'S.Y.M.C.A.']  # Example list for postgraduate
        else:
            class_list = []  # Empty list if no option is selected
        
        context = {'class_list': class_list,'page':2}
        # Pass the class_list to the template context
    else:
        context={'page':1}
    return render(request,'base/form.html',context)

def form(request,pk):
    a = Application.objects.filter(pk=pk)
    if(request.user!=a[0].user):
        messages.error(request,'Invalid')
        return redirect('home')
    if(request.method=='POST'):
        form = ApplicationForm(request.POST,instance=a[0])
        if form.is_valid():
            form.save()
        else:
            messages.error(request,'Invalid Data Format')
    form = ApplicationForm(instance=a[0])
    return render(request,'base/form.html',{'page':3,"form":form})

def yourForms(request):
    forms = Application.objects.filter(user = request.user)
    return render(request,'base/yourForm.html',{"forms":forms})