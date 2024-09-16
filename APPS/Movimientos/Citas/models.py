from django.db import models
from APPS.Movimientos.Patients.models import Patients
from APPS.Movimientos.MedicalStaff.models import MedicalStaff
# Create your models here.

# Create your models here.
class Citas(models.Model):
    IdPatients = models.ForeignKey(Patients, on_delete=models.RESTRICT)
    MedicalStaffId = models.ForeignKey(MedicalStaff, on_delete=models.RESTRICT)
    CodeQuotes = models.CharField(max_length=10)
    Reason = models.TextField(max_length=500)
    State = models.CharField(max_length=50)
    DateTime = models.DateTimeField(null=False)
    Active = models.BooleanField()

    class Meta:
        db_table = 'Citas'


    def __str__(self):
        return self.CodeQuotes