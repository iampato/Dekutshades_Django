from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import  subscribeForm
from django.contrib import messages
from .models import Post,subscriber


def post_list_view(request):
    object_list = Post.published.all()    
    paginator = Paginator(object_list, 4) # 3 posts in each page   
    page = request.GET.get('page')
    try:      
        posts = paginator.page(page)
    except PageNotAnInteger:    # If page is not an integer deliver the first page
        posts = paginator.page(1)    
    except EmptyPage:        # If page is out of range deliver last page of results        
        posts = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = subscribeForm(data=request.POST)

        if form.is_valid():
            
            message = form.save(commit=False)
            if subscriber.objects.filter(Email = message.Email).exists():
                messages.warning(request,  "Your Email already exists in our Databases")
            else:
                message.save()

                Name = request.POST.get( 'Name', '')
                Email = request.POST.get( 'Email', '') 
                Subject = 'Welcome to DekutShades'
                message = 'Dear %s \nWelcome to dekutshades, Thanks for Subscribing to our mail.\n By signing up you agree with our terms and Conditions where they apply. ' %(Name)
                emailFrom =  settings.EMAIL_HOST_USER 
                emailTo =  Email 
                
                print (message)
                
                send_mail(Subject,message,emailFrom,[emailTo],fail_silently=False)
                #send_mail('hello','testing','wpwaweru858@yahoo.com',['858wpwaweru@gmail.com'],fail_silently=False)
                messages.success(request,  "You Successfully subscribed")

        return redirect('/blog')

    else:
        form = subscribeForm()    
    return render(request,'blog/post/list.html',{'page': page,'form':form,'posts': posts})

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

 
#def post_list_view(request):
#    posts = Post.published.all()
#    return render(request, 'blog/post/list.html', {'posts': posts})