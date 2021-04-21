from django.db import models
from phone_field import PhoneField


# Create your models here.
class Users(models.Model):
    name = models.TextField(max_length=60)
    email_id = models.EmailField()
    contact = PhoneField(blank=True, help_text='Contact number')