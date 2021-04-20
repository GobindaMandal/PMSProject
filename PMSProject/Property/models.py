from django.db import models

# Create your models here.

class Destination(models.Model):
   name = models.CharField(max_length=100, default="")
   Property_ID = models.IntegerField(default=0)
   email_address = models.CharField(max_length=500, default="")

