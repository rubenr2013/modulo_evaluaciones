from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from aprendices.models import Aprendiz, Curso


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

    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE, related_name='evaluaciones', verbose_name='Aprendiz')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='evaluaciones', verbose_name='Curso', null=True, blank=True)
    tipo = models.CharField(max_length=3, choices=TIPO_EVALUACION_CHOICES, default='TEO', verbose_name='Tipo')
    descripcion = models.TextField(verbose_name='Descripción')
    fecha = models.DateField(verbose_name='Fecha')
    nota = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        verbose_name='Nota'
    )
    estado = models.CharField(max_length=3, choices=ESTADO_EVALUACION_CHOICES, default='PEN', verbose_name='Estado')
    observaciones = models.TextField(blank=True, null=True, verbose_name='Observaciones')

    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"
        ordering = ['-fecha']
        indexes = [
            models.Index(fields=['-fecha']),
            models.Index(fields=['aprendiz', 'curso']),
        ]

    def clean(self):
        super().clean()
        # Validar que el aprendiz esté inscrito en el curso si se especifica curso
        if self.curso and self.aprendiz:
            if not self.curso.aprendices.filter(id=self.aprendiz.id).exists():
                raise ValidationError({
                    'aprendiz': 'El aprendiz seleccionado no está inscrito en el curso especificado.'
                })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        curso_info = f" - {self.curso.codigo}" if self.curso else ""
        return f"{self.aprendiz} - {self.get_tipo_display()} - {self.fecha}{curso_info}"
