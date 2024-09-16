
from django.contrib import admin
from APPS.Movimientos.Tutors.models import Tutors
@admin.register(Tutors)

class TutorsAdmin(admin.ModelAdmin):
    list_display = ['CodeTutor', 'Occupation', 'Active']
    search_fields = ['PatientCode']