from typing import Any

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class AccountManager(BaseUserManager):
    """AccountManager class."""

    use_in_migrations = True

    def _create_user(self, email: str, username: str, password: str, **extra_fields: Any) -> Any:
        values = [email, username]
        field_value = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value.items():
            if not value:
                raise ValueError("The {} value must be set".format(field_name))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        now = extra_fields.get("date_joined", timezone.now())
        user.date_joined = now
        user.save(using=self._db)
        return user

    def create_user(self, email: str, username: str, password: str, **extra_fields: Any) -> Any:
        """Create user method."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email: str, username: str, password: str, **extra_fields: Any) -> Any:
        """Create super user method."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **extra_fields)
