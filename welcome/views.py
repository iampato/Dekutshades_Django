import os
from django.shortcuts import render
from .models import Girl, Guy ,Fresher
from django.conf import settings
from django.http import HttpResponse
from . import database
from .models import PageView

#openshift needs this
def index(request):
	hostname = os.getenv('HOSTNAME', 'unknown')
	PageView.objects.create(hostname=hostname)

	return render(request, 'home/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
# upt to this


def girl_view(request):
	girls = Girl.published.all()
	return render(request, 'home/post/girls.html', {'girls': girls})
def guy_view(request):
	guys = Guy.published.all()
	return render(request, 'home/post/guys.html', {'guys': guys})
def fresher_view(request):
	freshers = Fresher.published.all()
	return render(request, 'home/post/freshers.html', {'freshers': freshers})


