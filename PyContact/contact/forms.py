from django import forms

class Contacts(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()

