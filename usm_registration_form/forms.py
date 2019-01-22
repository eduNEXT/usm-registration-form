"""
Model forms file.
"""
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import CustomFormFields


class CustomForm(ModelForm):
    """
    Class to defined the form used from CustomFormFields model.
    """
    class Meta(object):
        """
        Class to initialize the form.
        """
        model = CustomFormFields
        fields = (
            'rut',
        )

    def __init__(self, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)
        self.fields['rut'].error_messages = {
            "invalid": _("RUT Format without periods: '99999999-k'."),
            "required": _('Please add your RUT.')
        }

