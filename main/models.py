from django.db import models


# Create your models here.

class Client(models.Model):
    nom = models.CharField(max_length=50,null=False)
    prenom = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=False)
    mot_de_passe = models.CharField(max_length=50,null=False)