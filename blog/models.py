from django.db import models

# Create your models here.
class Post(models.Model):
	blog_title = models.CharField(max_length=300,)
	blog_data = models.DateTimeField()
	blog_text = models.TextField()
	blog_image = models.ImageField(upload_to='event_images/')
