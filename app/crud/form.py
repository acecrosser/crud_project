from django import forms
from users.models import User


class UpUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
        }

        widgets = {
            'password': forms.PasswordInput(),
        }
