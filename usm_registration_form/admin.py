# -*- coding: utf-8 -*-
"""
Admin file.
"""
from django.contrib import admin
from .models import CustomFormFields
from django.utils.translation import ugettext_lazy as _

@admin.register(CustomFormFields)
class CustomFormFieldsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)

class CustomFormFieldsInline(admin.StackedInline):
    """ Inline admin interface for CustomFormFields model. """
    model = CustomFormFields
    can_delete = False
    verbose_name_plural = _('Custom Fields')
