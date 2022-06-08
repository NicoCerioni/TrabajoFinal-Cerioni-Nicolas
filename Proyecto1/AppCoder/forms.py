from email.policy import default
from django.forms import ImageField, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date
from .models import *

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserLoginForm(forms.Form):
    username = forms.CharField(label= 'Nombre de usuario')
    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)

class PostForm(forms.Form):
    title = forms.CharField(label= 'Título', max_length=100)
    subtitle = forms.CharField(label= 'Subtítulo', max_length=100, required=False)
    content = forms.CharField(label= 'Contenido', widget=forms.Textarea)
    date = forms.DateField(label= 'Fecha', initial=date.today())
    image = ImageField(label= 'Imagen', required=False)

class UpdateUserForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email= forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class MessageForm(forms.Form):
    message = forms.CharField(label= 'Mensaje', widget=forms.Textarea)
    emisor = forms.CharField(label= 'Emisor', widget=forms.TextInput(attrs={'class':'form-control'}))
    receptor = forms.CharField(label= 'Receptor', widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(label= 'Fecha', initial=date.today())


class UploadImageForm(forms.Form):
    
    class Meta:
        model = post
        fields = ['image']


class Link(forms.Form):
    link= forms.CharField(label= 'Link', widget=forms.TextInput(attrs={'class':'form-control'}))
    

  