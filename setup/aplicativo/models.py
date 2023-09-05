from datetime import datetime
from django.db import models



# Create your models here.
class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    description =  models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="Imagem")
    

class Main (models.Model):
    titulo2 = models.CharField(max_length=200)
    description2 =models.CharField(max_length=200)
    imagem2 = models.ImageField(upload_to="image")

class Main2 (models.Model):
    titulo3 = models.CharField(max_length=200)
    description3 =models.CharField(max_length=200)
    imagem3 = models.ImageField(upload_to="image")
    icones =models.ImageField(upload_to="image")


class footer (models.Model):
    titulo4 = models.CharField(max_length=200)
    description4 =models.CharField(max_length=200)
    imagem4 = models.ImageField(upload_to="image")
    icones2 =models.ImageField(upload_to="image")



