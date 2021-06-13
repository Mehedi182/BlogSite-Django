from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField(null=True,blank=True)
    img = models.CharField(max_length=2083)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']