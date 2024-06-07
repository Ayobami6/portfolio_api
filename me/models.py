from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from utils.decorators import str_meta

# Create your models here.


@str_meta
class ME(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = PhoneNumberField(blank=True, null=True)
    pronouns = models.CharField(max_length=50)
    current_focus = models.CharField(max_length=100, blank=True, null=True)
    fun_fact = models.TextField(null=True, blank=True)


@str_meta
class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)
    me = models.ForeignKey(ME, on_delete=models.CASCADE, related_name="plangs")


@str_meta
class Interest(models.Model):
    name = models.CharField(max_length=50)
    me = models.ForeignKey(ME, on_delete=models.CASCADE, related_name="interests")


@str_meta
class Technologies(models.Model):
    name = models.CharField(max_length=50)
    me = models.ForeignKey(ME, on_delete=models.CASCADE, related_name="technologies")


@str_meta
class Education(models.Model):
    name = models.CharField(max_length=50)
    me = models.ForeignKey(ME, on_delete=models.CASCADE, related_name="educations")
