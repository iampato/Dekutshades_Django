from .models import Messages
from django import forms
from django.forms import ModelForm


class ContactForm(forms.ModelForm):
	class Meta:
		model = Messages
		fields = ('Name','Phone', 'Email', 'Message')
		def clean(self):
			data = self.cleaned_data
	
			Name = data.get('Name')
			Phone = data.get('Phone')
			Email = data.get('Email')
			Message =data.get('Message')
			if not Name and not Phone and not Email and not Message:
				raise forms.ValidationError ('You have to write something!')
			return data


