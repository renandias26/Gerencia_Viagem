from django.db import models
    
class Travel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    dateCome = models.DateField()
    dateLeave = models.DateField()
    
class Destiny:
    name = models.CharField(max_length=100)