from django.contrib import admin
from .models import Messages

class MessageAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Email', 'Phone','Message', 'sent_on')
	list_filter = ( 'active','sent_on', 'updated')
	search_fields = ('Name', 'Email', 'Message')
admin.site.register(Messages, MessageAdmin)