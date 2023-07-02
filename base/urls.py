from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('fillform/',views.fillFormPage,name='fillform'),
    path('form/<str:pk>/',views.form,name='form'),
    # path('form/',views.form,name='form'),
    path('yourForms/',views.yourForms,name='yourForms'),
]
