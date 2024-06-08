from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from utils.decorators import str_meta

# Create your models here.


@str_meta
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    source_code_link = models.URLField(
        default="https://github.com/Ayobami6/portfolio_api"
    )


# TODO: Add Tools inline model to Project
