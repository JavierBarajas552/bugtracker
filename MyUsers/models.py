from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    name = models.CharField(max_length=80, blank=True, null=True)
