from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.core.mail import send_mail
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

            
            Name = form.cleaned_data['Name']
            Phone = form.cleaned_data['Phone']
            Message = form.cleaned_data['Message']
            Subject = 'Welcome to DekutShades'

            emailFrom =  form.cleaned_data['Email'] 
            emailTo =  settings.EMAIL_HOST_USER
           
            send_mail(Subject,Name,Phone,Message,emailFrom,[emailTo],fail_silently=False)

            instance = contact.save(commit=False)
            instance.save()
            messages.success(request,
				"Your message has been successfully Been sent")
            
            return redirect('/contact')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })








