from django.contrib import admin
from APPS.Movimientos.Citas.models import Citas
# Register your models here.

@admin.register(Citas)

class CitasAdmin(admin.ModelAdmin):
    list_display = ['IdPatients','CodeQuotes', 'Reason', 'State', 'DateTime', 'Active']
    search_fields = ['CodeQuotes']