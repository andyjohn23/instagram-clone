from django import forms
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required valid emailaddress')

    class Meta:
        model = UserAccount
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = UserAccount.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(f'Email {email} is already in use!')


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = UserAccount.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f'Username {username} is already in use!')