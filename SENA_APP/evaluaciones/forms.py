from django import forms
from .models import Evaluacion


class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['aprendiz', 'curso', 'tipo', 'descripcion', 'fecha', 'nota', 'estado', 'observaciones']
        labels = {
            'aprendiz': "Aprendiz",
            'curso': "Curso",
            'tipo': "Tipo de Evaluación",
            'descripcion': "Descripción",
            'fecha': "Fecha",
            'nota': "Nota (0-5)",
            'estado': "Estado",
            'observaciones': "Observaciones",
        }
        widgets = {
            'aprendiz': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '5'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        aprendiz = cleaned_data.get('aprendiz')
        curso = cleaned_data.get('curso')

        # Validar que si se especifica un curso, el aprendiz esté inscrito en él
        if curso and aprendiz:
            if not curso.aprendices.filter(id=aprendiz.id).exists():
                raise forms.ValidationError(
                    f"El aprendiz {aprendiz.nombre_completo()} no está inscrito en el curso {curso.nombre}."
                )

        return cleaned_data

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if nota is not None and (nota < 0 or nota > 5):
            raise forms.ValidationError("La nota debe estar entre 0 y 5.")
        return nota
