from django.db import models

class Message(models.Model):
	Name = models.CharField(max_length=80)
	Phone = models.CharField(max_length=11)
	Email = models.EmailField()
	Message = models.TextField()
	sent_on = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)


	class Meta:
		ordering = ('sent_on',)

	def __str__(self):
 		return self.Email
 
