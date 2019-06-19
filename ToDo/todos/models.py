from django.db import models
from datetime import datetime

# Create your models here.
class todomodel(models.Model):
    author = models.CharField(max_length = 32)
    Title = models.CharField(max_length = 32)
    Discription = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default = datetime.now,blank = True)
