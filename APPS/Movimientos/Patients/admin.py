
# Register your models here.
from django.contrib import admin
from APPS.Movimientos.Citas.models import Patients


# Register your models here.

@admin.register(Patients)

class PatientsAdmin(admin.ModelAdmin):
    list_display = ['PatientCode', 'Birthdate', 'Allergies', 'Active']
    search_fields = ['PatientCode']