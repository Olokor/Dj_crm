from email.policy import default

from django import forms

class LeadForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age'}))