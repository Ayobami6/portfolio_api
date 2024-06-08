from django.db import models
from utils.decorators import str_meta

# Create your models here.


@str_meta
class BlogPost(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField()
