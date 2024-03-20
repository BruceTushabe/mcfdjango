from django import forms
from django.forms.models import modelform_factory

from core.models import Client_Account  # Import model form factory


class SearchForm(forms.Form):
    account_number = forms.CharField(label='Account Number')


"""class ClientInfoForm(forms.Form):
    def ClientInfoForm(client_account):
        #    Creates a dynamic form based on the provided client_account instance.

    Args:
        client_account (django.db.models.Model): The client account object.

    Returns:
        django.forms.Form: A dynamically generated form based on the client account's fields.
        #

    fields = {}
    for field in client_account._meta.get_fields():
        if not getattr(client_account, field.name):
            # Only include fields with None values
            field_instance = field
            fields[field.name] = forms.CharField(label=field.verbose_name, required=False)  # Set required=False for optional fields

        return type('ClientInfoForm', (forms.Form,), {'fields': fields})"""

# Alternative using model form factory (recommended):
from django import forms

class ClientInfoForm(forms.Form):
    """
    Form for editing client information, dynamically generated with fields
    that are currently null in the database.
    """

    def __init__(self, client_account, *args, **kwargs):
        super(ClientInfoForm, self).__init__(*args, **kwargs)

        self.fields = {}  # Clear any existing fields

        for field in client_account._meta.get_fields():
            if not getattr(client_account, field.name):
                # Only include fields with None values
                field_instance = field
                self.fields[field.name] = forms.CharField(label=field.verbose_name, required=False)

    
