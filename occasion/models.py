

# Create your models here.
from django.db import models

class itemtype(models.Model):
    type = models.CharField(max_length=150,null=True)
    description = models.CharField(max_length=150,null=True)
    
    
    def __str__(self):
        return self.type

class tag(models.Model):
    tag = models.CharField(max_length=150,null=True)
    description = models.CharField(max_length=150,null=True)
    
    
    def __str__(self):
        return self.tag

class occasion(models.Model):
    occasion = models.CharField(max_length=150,null=True)
    description = models.CharField(max_length=150,null=True)
    itemtype = models.ForeignKey(itemtype, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(tag)

    def __str__(self):
        return self.occasion

