from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    class Meta:
        ordering = ['pub_date']