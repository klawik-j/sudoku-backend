from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    """Admin account."""

    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account

    list_display = ("email", "username", "is_staff", "is_superuser")
    list_filter = ("email", "username", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("email", "username", "password1", "password2", "is_staff", "is_active")},
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
