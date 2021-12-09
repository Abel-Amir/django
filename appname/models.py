from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    commentauthor = models.CharField(max_length= 300)
