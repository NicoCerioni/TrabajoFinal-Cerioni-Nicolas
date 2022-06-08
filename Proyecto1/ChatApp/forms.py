from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import date

class MessageForm(forms.Form):
    message = forms.CharField(label= 'Mensaje', widget=forms.Textarea)
    emisor = forms.CharField(label= 'Emisor', widget=forms.TextInput(attrs={'class':'form-control'}))
    receptor = forms.CharField(label= 'Receptor', widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.DateField(label= 'Fecha', initial=date.today())