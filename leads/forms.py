from email.policy import default

from django import forms

from leads.models import Lead


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            "age",
            "agent"

        )

class LeadForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Age'}))