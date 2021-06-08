from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    img = models.CharField(max_length=2083)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']