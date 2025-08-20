from django.db import models
from aprendices.models import Aprendiz

class Evaluacion(models.Model):
    TIPO_EVALUACION_CHOICES = [
        ('TEO', 'Teórica'),
        ('PRA', 'Práctica'),
        ('PRO', 'Proyecto'),
    ]

    ESTADO_EVALUACION_CHOICES = [
        ('PEN', 'Pendiente'),
        ('REA', 'Realizada'),
        ('COR', 'Corregida'),
    ]

    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE, related_name='evaluaciones')
    tipo = models.CharField(max_length=3, choices=TIPO_EVALUACION_CHOICES, default='TEO')
    descripcion = models.TextField()
    fecha = models.DateField()
    nota = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    estado = models.CharField(max_length=3, choices=ESTADO_EVALUACION_CHOICES, default='PEN')
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.aprendiz} - {self.get_tipo_display()} - {self.fecha}"
