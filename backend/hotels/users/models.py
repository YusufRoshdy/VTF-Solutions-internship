from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16)