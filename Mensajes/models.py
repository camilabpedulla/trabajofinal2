from datetime import datetime
from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Mensajes(models.Model):
    texto = models.CharField(max_length=500)
    emisor = models.CharField(max_length=150)
    receptor = models.CharField(max_length=150)
    fecha = models.DateTimeField()
