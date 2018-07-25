from .models import Messages
from django import forms


class ContactForm(forms.ModelForm):
	class Meta:
		model = Messages
		fields = ('Name','Phone', 'Email', 'Message')
		def clean(self):
			clean_data = super(ContactForm,self).clean()
			Name = clean_data.get('Name')
			Phone = clean_data.get('Phone')
			Email = clean_data.get('Email')
			
			Message = clean_data.get('Message')
			if not Name and not Phone and not Email and not Message:
				raise forms.ValidationError ('You have to write something!')


