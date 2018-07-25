from .models import subscribe
from django import forms


class subscribeForm(forms.ModelForm):
	class Meta:
		model = subscribe
		fields = ('Name','Email')