# -*- coding: utf-8 -*-
"""
File to define CustomFormFields model.
"""

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CustomFormFields(models.Model):
    """
    Holds extra info to be, used during
    user registration as a form extension.
    """
    user = models.OneToOneField(USER_MODEL, null=True)

    rut_regex = RegexValidator(
        regex=r'^\d{8}-[a-zA-Z0-9]$',
        message=_("RUT Format without periods: '99999999-k'.")
        )
    rut = models.CharField(
        verbose_name=_("RUT"),
        validators=[rut_regex],
        max_length=11,
    )
