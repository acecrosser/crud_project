from django import forms
from users.views import User


class RegistrationUser(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']