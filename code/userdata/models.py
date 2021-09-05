from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from django.utils.translation import ugettext_lazy as _

from .managers import AccountManager

# Create your models here.

class Account(AbstractUser):
    username = models.CharField(_('Username'), max_length=30, unique=True,
                                help_text=_(
                                    'Enter unique username - 30 characters or '
                                    'fewer. '
                                    'Letters, digits and _ only.'),
                                validators=(RegexValidator(r'^\w+$',
                                                           _(
                                                               'Enter a valid '
                                                               'username. '
                                                               'This value '
                                                               'may contain '
                                                               'only '
                                                               'letters, '
                                                               'numbers and _ '
                                                               'character.'),
                                                           'invalid'),),
                                error_messages={'unique': _(
                                    'The username is already taken.'), })
    email = models.EmailField(_('E-mail address'), validators=[EmailValidator],
                              unique=True,
                              help_text=_('Enter unique e-mail address.'),
                              error_messages={'unique': _(
                                  'User with this e-mail already exists.'), })

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    def __str__(self):
        return f'{self.username} account'

    class Meta:
        abstract = False
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

