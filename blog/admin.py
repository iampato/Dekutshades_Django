from django.contrib import admin
from .models import Post,subscriber

class subscriberAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Email', 'sent_on')
	list_filter = ( 'active','sent_on', 'updated')
	search_fields = ('Name', 'Email')
admin.site.register(subscriber, subscriberAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status','created')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','author')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    
admin.site.register(Post)