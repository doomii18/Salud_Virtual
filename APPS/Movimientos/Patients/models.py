from django.db import models

from APPS.Catalogos.Person.models import Person
# Create your models here.

class Patients(models.Model):
    IdPerson = models.ForeignKey(Person, on_delete=models.RESTRICT)
    PatientCode = models.CharField(max_length=6, null=False)
    Birthdate = models.DateField(null=False)
    Allergies = models.TextField(max_length=200, null=True)
    Active = models.BooleanField()

    class Meta:
        db_table = 'Patient'

    def __str__(self):
        return self.PatientCode