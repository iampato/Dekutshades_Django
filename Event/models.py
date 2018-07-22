from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    PAYMENT_CHOICES = (
        ('free', 'Free'),
        ('not Free', 'Not free'),
    )
    title = models.CharField(max_length=250)
    image = models.FileField()
    location = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    body = models.TextField()
    payment = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default ='Free')
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

    