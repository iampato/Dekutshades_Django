from django.shortcuts import render
from .models import Girl, Guy ,Fresher

def list_view(request):
    return render(request, 'home/index.html',)

def girl_view(request):
	girls = Girl.published.all()
	return render(request, 'home/post/girls.html', {'girls': girls})
def guy_view(request):
	guys = Guy.published.all()
	return render(request, 'home/post/guys.html', {'guys': guys})
def fresher_view(request):
	freshers = Fresher.published.all()
	return render(request, 'home/post/freshers.html', {'freshers': freshers})


