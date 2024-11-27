from django.contrib.auth.forms import UserCreationForm
from .models import User
from apps.account.models import Account

class FormNewUser(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'dni', 'img_profile']
    
    def save(self, commit = True):
        if commit:
            user = super().save()
            Account.objects.create(user=user)
        return user