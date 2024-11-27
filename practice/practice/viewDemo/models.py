from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    is_staff = models.BooleanField(default=False)
    email = models.EmailField()
    