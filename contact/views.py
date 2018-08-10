from django.shortcuts import render
from django.contrib import messages
from .forms import  ContactForm


def contact(request): 
	if request.method == 'POST':
		form = ContactForm(data=request.POST)

		if form.is_valid():
			message = form.save(commit=False)
			message.save()
			messages.success(request,
				"Your message has been sent Successfully!!")
	else:
		form = ContactForm() 
	return render(request, 'contact/contact.html',{'form':form,})
