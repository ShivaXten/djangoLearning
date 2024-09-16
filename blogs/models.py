from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField  # Import RichTextField

class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Blog_images/', blank=True)
    content = RichTextField(max_length=10000)  # Use RichTextField instead of TextField
    blogDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):    
        return f"{self.title} written by {self.user.username}"
