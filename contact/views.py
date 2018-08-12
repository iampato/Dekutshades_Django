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
            Email = form.cleaned_data['Email'] 
            Message = form.cleaned_data['Message']
            Subject = 'DekutShades Contact '

            text = "Dear Patrick,\nSomeone used the dekutshades contact form.\nHere is what was submited:\n %s\n %s\n %s\n %s\n You received this mail, because you are the admin." %(Name,Phone,Email,Message)
            emailFrom =  settings.EMAIL_HOST_USER 
            emailTo =  '858wpwaweru@gmail.com'
           
            send_mail(Subject,text,emailFrom,[emailTo],fail_silently=False)
            instance = contact.save(commit=False)
            instance.save()
            messages.success(request,
				"Your message has been successfully Been sent")
            
            return redirect('/contact')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })








