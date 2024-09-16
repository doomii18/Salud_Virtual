
from django.db import models

# Create your models here.
from APPS.Movimientos.Patients.models import Patients


# Create your models here.
class Record(models.Model):
    IdPatients = models.ForeignKey(Patients, on_delete=models.RESTRICT)
    CodeRecords = models.CharField(max_length=6, null=False)
    Diagnosis = models.TextField(max_length=500, null=False)
    Treatment = models.TextField(max_length=500, null=False)
    Forecast = models.CharField(max_length=200, null=False)
    Date = models.DateField(null=False)
    WeightPounds = models.IntegerField(null = True)
    Measure = models.IntegerField(null =True)

    Active = models.BooleanField()

    class Meta:
        db_table = 'Record'

    def __str__(self):
        return f'{self.CodeRecords} - {self.Date}'
