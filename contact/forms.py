from django.forms import ModelForm
from django import forms
from .models import Message

# our new form
class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Phone = forms.CharField(max_length=10)
    Email = forms.EmailField(required=True)
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class messageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('Name','Phone', 'Email', 'Message')
        


