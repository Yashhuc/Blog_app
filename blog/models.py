from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
    # get url method is to find the url of the specific instance of the post model object
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
