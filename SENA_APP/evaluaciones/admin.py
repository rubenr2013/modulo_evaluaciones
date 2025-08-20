from django.contrib import admin
from .models import Evaluacion

@admin.register(Evaluacion)
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = ('aprendiz', 'get_tipo_display', 'fecha', 'nota', 'get_estado_display')
    list_filter = ('tipo', 'estado', 'fecha')
    search_fields = ('aprendiz__nombre', 'aprendiz__apellido', 'descripcion')
