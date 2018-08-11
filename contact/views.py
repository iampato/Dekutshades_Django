from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from .forms import  messageForm

# add to your views
def contact(request):
    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)
        contact = messageForm(data=request.POST)

        if form.is_valid():

            Name = request.POST.get( 'Name', '')
            Phone = request.POST.get('Phone', '')
            Email = request.POST.get( 'Email', '')
            Message = request.POST.get('Message', '')

            # Email the profile with the
            # contact information
            template =get_template('contact/contact_template.txt')
            context = {
                'Name': Name,
                'Phone': Phone,
                'Email': Email,
                'Message': Message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': Email }
            )
            email.send()

            instance = contact.save(commit=False)
            instance.save()
            messages.success(request,
				"Your message has been successfully Been sent")
            
            return redirect('/contact')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })










'''
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Messages


def contact(request): 
	if request.method == 'POST':
		form = ContactForm(data=request.POST)

		if form.is_valid():
			Name = request.POST.get('Name', '' )
			Phone = request.POST.get('Phone', '' )
			Email = request.POST.get('Email', '' )
			Message = request.POST.get('Message', '' )

			message = form.save(commit=False)
			message.save()
			messages.success(request,
				"Your message has been sent Successfully!!")
			

			return redirect('contact')
	else:
		form = ContactForm() 
	return render(request, 'contact/contact.html',{'form':form,})
'''