from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from utils.decorators import str_meta

# Create your models here.


@str_meta
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = CKEditor5Field("Text", config_name="extends")
    link = models.URLField()
    source_code_link = models.URLField(
        default="https://github.com/Ayobami6/portfolio_api"
    )
