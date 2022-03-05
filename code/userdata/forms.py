from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Account


class AccountCreationForm(UserCreationForm):
    """Account creation form."""

    class Meta:
        model = Account
        fields = ("email",)


class AccountChangeForm(UserChangeForm):
    """Account change form."""

    class Meta:
        model = Account
        fields = ("email",)
