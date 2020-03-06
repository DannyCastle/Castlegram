from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    #https://docs.djangoproject.com/en/3.0/ref/models/fields/#imagefield
    #Pillow must be installed
    #upload = models.ImageField(upload_to='\fillthis in\')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
