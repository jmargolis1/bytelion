from django.db import models

# Create your models here.

class Scratcher(models.Model):
    # name of scratcher
    name = models.CharField(max_length=255, null=False)
    # desc of scratcher 
    des = models.CharField(max_length=255, null=False)
    # size of scratcher 
    size = models.CharField(max_length=255, null=False)
    # price of scratcher 
    price = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.des, self.size, self.price)