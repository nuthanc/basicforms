from django import forms
from django.core import validators

def start_with_n(value):
    if value[0].lower() != 'n':
        raise forms.ValidationError("NAME NEEDS TO START WITH N")

class FormName(forms.Form):
    name = forms.CharField(validators=[start_with_n])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    botCatcher = forms.CharField(required=False,
     widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

