from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url('blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url('event/', include('Event.urls', namespace='Event', app_name='Event')),
    url('contact/', include('contact.urls', namespace='contact', app_name='contact')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
