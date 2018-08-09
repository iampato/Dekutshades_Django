from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from tinymce import HTMLField

class subscribe(models.Model):
    Name = models.CharField(max_length=80)
    Email = models.EmailField()
    sent_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('sent_on',)

    def __str__(self):
        return self.Email
 
# Custom Manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

# Our Post Model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.FileField()
    author = models.ForeignKey(User, related_name='blog_posts')
    content = HTMLField('Content')
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
    
    def get_absolute_url(self):
        return reverse('blog:post_detail_view', args=[self.publish.year, self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

   
