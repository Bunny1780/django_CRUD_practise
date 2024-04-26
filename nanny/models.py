from django.db import models

# Create your models here.
class Nanny(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    description = models.TextField(default='')