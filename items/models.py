from django.db import models

# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)

def __str__(self) -> str:
    return self.item_name + " " + self.description