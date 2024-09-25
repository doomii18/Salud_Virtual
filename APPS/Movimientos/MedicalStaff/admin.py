from django.contrib import admin
from APPS.Movimientos.MedicalStaff.models import MedicalStaff
# Register your models here.

@admin.register(MedicalStaff)

class MedicalStaffAdmin(admin.ModelAdmin):
    list_display = ['IdPerson', 'MedicalStaffCode', 'Active']
    search_fields = ['MedicalStaffCode']