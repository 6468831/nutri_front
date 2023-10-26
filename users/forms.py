from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

class UserCreationForm(forms.Form):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "id": "sign-up-email"}),)
    password1 = forms.CharField(
        label=("Password1"),
        max_length=254,
        widget=forms.TextInput(attrs={"id": "password1"}),)
    password2 = forms.CharField(
        label=("Password2"),
        max_length=254,
        widget=forms.TextInput(attrs={"id": "password2"}),)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name in ["invalid_name_1", "invalid_name_2"]: # etc.
            raise ValidationError("Forbidden value for this field.")
        return name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})