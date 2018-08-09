from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Custom Manager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

# Our ladies Model
class Girl(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    image = models.FileField()
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	
    # The default manager
    objects = models.Manager()
    # Custom made manager
    published = PublishedManager()
    class Meta:
        ordering = ('-title',)
        verbose_name = 'girl'
        verbose_name_plural = 'girls'

    def __str__(self):
        return self.title


# Our Guys Model
class Guy(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    image = models.FileField()
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # The default manager
    objects = models.Manager()
    # Custom made manager
    published = PublishedManager()
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title
    
# Our freshers Model
class Fresher(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    image = models.FileField()
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    # The default manager
    objects = models.Manager()
    # Custom made manager
    published = PublishedManager()
    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title

class slider(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250,default='slider')
    image = models.FileField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    # The default manager
    objects = models.Manager()
    # Custom made manager
    published = PublishedManager()

    class Meta:
        ordering = ('-title',)
    def __str__(self):
        return self.title