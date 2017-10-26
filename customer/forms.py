from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import *

def clean_contact_no(phone):
    try:
        if phone:
            min_length = 10
            max_length = 15
            ph_length=len(str(phone))
            if ph_length < min_length or ph_length > max_length:
                raise ValidationError('Contact number length is not valid!')
    except(ValueError, TypeError):
        raise ValidationError("Please enter a valid contact number!")
    return phone

class CustomerForm(ModelForm):
    phone = forms.IntegerField(validators=[clean_contact_no], widget=forms.NumberInput(attrs={'required': "required"}))

    class Meta:
        model = Customer
        widgets={
            "name": forms.TextInput(attrs={'required': "required"}),
            "age": forms.NumberInput(attrs={'required': "required"}),
            "street": forms.TextInput(attrs={'required': "required"}),
            "city": forms.TextInput(attrs={'required': "required"}),
            "state": forms.TextInput(attrs={'required': "required"}),
            "country": forms.TextInput(attrs={'required': "required"}),
            "pin_code": forms.NumberInput(attrs={'required': "required"}),
            "balance":forms.NumberInput(attrs={'required': "required"}),
        }
        fields=['name','age','phone','street','city','state','country','pin_code','balance']