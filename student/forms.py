from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import get_user_model,authenticate
user=get_user_model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

   
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
                raise forms.ValidationError('email already exist') 
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('This user does not exist')
        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password')
        if not user.is_active:
            raise forms.ValidationError('This user is not active')