from .models import subscriber

from django import forms


class subscribeForm(forms.ModelForm):
	class Meta:
		model = subscriber
		fields = ('Name','Email')