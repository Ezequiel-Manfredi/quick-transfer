from django import forms
from .models import User

class FormNewUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'dni', 'img_profile']