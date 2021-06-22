from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    utilisteur = models.OneToOneField(User,null=False,on_delete=models.CASCADE,default=None)
    photo = models.ImageField(null=True,default=None)
    cv = models.expressions.ExpressionList 
    cv = models.expressions.ExpressionList


class Contest(models.Model):
    choises = (('facile','facile'),('normal','normal'),('difficile','difficile'))

    ID = models.IntegerField(primary_key=True)
    enonce = models.TextField(max_length=10000000,null=False)
    name = models.CharField(max_length=50,null=False)
    auteur = models.CharField(max_length=20,null=False,default="admin")
    date = models.DateTimeField(null=False)
    dure = models.DateTimeField()
    niveau = models.CharField(max_length=20,null=False,choices=choises)
    input = models.FloatField()
    output = models.FloatField()
    