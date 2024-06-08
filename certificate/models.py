from django.db import models
from utils.decorators import str_meta

# Create your models here.


@str_meta
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cert_file = models.FileField(upload_to="pdfs")
