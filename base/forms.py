from django.forms import ModelForm
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
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['user','className']