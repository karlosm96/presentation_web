import email
from django import forms
from .models import contacto_info

class ContactForm(forms.ModelForm):
    class Meta:
        model = contacto_info
        fields = ('first_name', 'last_name','email', 'message')