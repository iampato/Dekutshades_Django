from .models import Messages
from django import forms

class ContactForm(forms.ModelForm):
	class Meta:
		model = Messages
		fields = ('Name','Phone', 'Email', 'Message')



# 