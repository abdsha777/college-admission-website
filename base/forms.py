from django.forms import ModelForm,DateInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Application


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["mobile", "name", 'username',
                  'email', 'password1', 'password2']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", 'username', 'email']


# application forms
class ApplicationForm(ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Application
        fields = '__all__'
        # fields = ['birth_date']
        widgets = {
            'birth_date': DateInput(),
        }
        exclude = ['user','className','created','updated','status','last_fee_date']