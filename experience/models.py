from django.db import models
from utils.decorators import str_meta
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

# Create your models here.


@str_meta
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = CKEditor5Field("Text", config_name="extends")
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
