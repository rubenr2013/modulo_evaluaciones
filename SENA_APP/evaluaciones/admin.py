from django.contrib import admin
from .models import Evaluacion


@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('aprendiz', 'curso', 'get_tipo_display', 'fecha', 'nota', 'get_estado_display')
    list_filter = ('tipo', 'estado', 'fecha', 'curso')
    search_fields = ('aprendiz__nombre', 'aprendiz__apellido', 'curso__nombre', 'curso__codigo', 'descripcion')
    list_editable = ('nota', )
    date_hierarchy = 'fecha'

    fieldsets = (
        ('Información del Aprendiz y Curso', {
            'fields': ('aprendiz', 'curso')
        }),
        ('Detalles de la Evaluación', {
            'fields': ('tipo', 'descripcion', 'fecha')
        }),
        ('Calificación y Estado', {
            'fields': ('nota', 'estado', 'observaciones')
        }),
    )
