from django.db import models
    
class Travel(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    dateCome = models.DateField()
    dateLeave = models.DateField()
    
    def addDestiny(self, destinyName):
        Destiny.objects.create(name=destinyName, travel=self)
        pass

    def removeDestiny(self, destinyName):
        if Destiny.objects.all(travel=self).copy() == 1:
            return
        
        item = Destiny.objects.get(travel=self,name=destinyName)
        item.delete()
        pass

class Destiny(models.Model):
    name = models.CharField(max_length=100)
    travel = models.ForeignKey('Travel', on_delete=models.CASCADE)