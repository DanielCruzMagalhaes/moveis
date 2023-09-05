from datetime import datetime
from django.db import models



# Create your models here.
class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    description =  models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="Imagem")
    

class Main (models.Model):
    titulo = models.CharField(max_length=200)
    description =models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="image")

class Main2 (models.Model):
    titulo = models.CharField(max_length=200)
    description =models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="image")
    icones =models.ImageField(upload_to="image")


class footer (models.Model):
    titulo = models.CharField(max_length=200)
    description =models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="image")
    icones =models.ImageField(upload_to="image")



