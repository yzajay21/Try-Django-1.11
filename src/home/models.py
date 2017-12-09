from django.db import models

# Create your models here.
class Photo(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length =200)
	meta_keywords = models.CharField("Meta Keywords",max_length=255,
		 help_text='Comma-delimated set of SEO Keywords for meta tag',default=False)
	meta_description= models.CharField("Meta Description",max_length=255,
		help_text='Content for description meta tag',default=False)

	def __str__(self):
		return self.title
class Meta :
	ordering = ["title"]
