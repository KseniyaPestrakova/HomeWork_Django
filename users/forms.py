from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Укажите email")
    username = forms.CharField(max_length=50, required=True)
    usable_password = None
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

