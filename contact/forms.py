from .models import Messages
from django import forms
from django.forms import ModelForm


class ContactForm(forms.ModelForm):
	class Meta:
		model = Messages
		fields = ('Name','Phone', 'Email', 'Message')
		def clean(self):
			super(ContactForm, self).clean()
			Name = self.cleaned_data.get('Name')
			Phone = self.cleaned_data.get('Phone')
			Email = self.cleaned_data.get('Email')
			Message = self.clean_data.get('Message')
			if not Name and not Phone and not Email and not Message:
				raise forms.ValidationError ('You have to write something!')
			return self.cleaned_data


