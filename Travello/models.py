from django.db import models

# Create your models here.

class Desinations(models.Model) :

    name=models.CharField(max_length=20)
    img  =models.ImageField(upload_to="Pictures")
    desc = models.TextField()
    price= models.IntegerField()
    offere =models.BooleanField(default=False)
