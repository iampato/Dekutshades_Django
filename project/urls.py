from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('', include('welcome.urls', namespace='welcome', app_name='welcome')),
    url(r'^admin/', include(admin.site.urls)),
    url('blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url('event/', include('Event.urls', namespace='Event', app_name='Event')),
    url('contact/', include('contact.urls', namespace='contact', app_name='contact')),
]


if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

