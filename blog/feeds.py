from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.contrib.sitemaps.views import sitemap
 
class PostsFeed(Feed):
    title = 'Dekutshades Blog Feeds'
    link = '/blog/'
    description = 'Our latest Posts!'
 
    def items(self):
        return Post.published.all()[:5]
 
    def item_title(self, item):
        return item.title
 