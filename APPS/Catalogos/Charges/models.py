from django.db import models

# Create your models here.
from django.db import  models
class Charges(models.Model):
    ChargeCode = models.CharField(max_length=5)
    NameCharges = models.CharField(max_length=100)
    Active = models.BooleanField()

    class Meta:
        db_table = 'Charge'

    def __str__(self):
        return  self.NameCharges