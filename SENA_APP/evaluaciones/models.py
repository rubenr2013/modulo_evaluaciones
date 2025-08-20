from django.db import models

from aprendices.models import Aprendiz


# Create your models here.
class Evaluacion(models.Model):
    TIPO_EVALUACION_CHOICES = [
        ('TEO', 'Teoría'),
        ('PRA', 'Práctica'),  
        ('PRO', 'Proyecto'),
    ]

    ESTADO_EVALUACION_CHOICES = [
        ('PEN', 'Pendiente'),
        ('REA', 'Realizada'),
        ('COR', 'Corregida'),
    ]

    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE, related_name='evaluacioes')
    tipo = models.Charfield(max_length=3, choices=TIPO_EVALUACION_CHOICES, default='TEO')
    descripcion = models.TextField()
    nota = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    estado = models.CharField(max_length=3, choices=ESTADO_EVALUACION_CHOICES, default='PEN')
    obsercvaciones = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.aprendiz} - {self.get_tipo_display()} - {self.fecha}"

