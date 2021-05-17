from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class TCTUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    contact = models.CharField(max_length=20)


# Create your models here.
