from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
]