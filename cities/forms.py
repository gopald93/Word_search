from django import forms

class ContactForm(forms.Form):
    city_name = forms.CharField(max_length=30)
   