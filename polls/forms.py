from django import forms

class AddForm(forms.Form):
    soa = forms.CharField()
    sob = forms.CharField()
