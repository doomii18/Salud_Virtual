
from django.contrib import admin
from APPS.Movimientos.Record.models import Record
@admin.register(Record)

class RecordAdmin(admin.ModelAdmin):
    list_display = ['CodeRecords', 'Diagnosis', 'Treatment', 'Active', 'Date', 'WeightPounds', 'Measure', 'Active']
    search_fields = ['CodeRecords']