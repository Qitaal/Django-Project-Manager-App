from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'role'
        )
        field_classes = {'username': UsernameField}
