from django import forms
from .models import contacto_in

class ContactForm(forms.ModelForm):
    class Meta:
        model = contacto_in
        fields = ('name', 'phone','subject', 'email', 'message')
