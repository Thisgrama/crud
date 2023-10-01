from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    def short_content(self):
        if len(self.content) > 20:
            return self.content[:20] + '...'
        else:
            return self.content

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.title