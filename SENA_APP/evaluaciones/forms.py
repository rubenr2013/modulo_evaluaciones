from django import forms
from .models import Evaluacion

class EvaluacionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ['aprendiz', 'tipo', 'descripcion', 'fecha', 'nota', 'estado', 'observaciones']
        labels = {
            'aprendiz': "Aprendiz",
            'tipo': "Tipo de Evaluación",
            'descripcion': "Descripción",
            'fecha': "Fecha",
            'nota': "Nota",
            'estado': "Estado",
            'observaciones': "Observaciones",
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_nota(self):
        nota = self.cleaned_data.get('nota')
        if nota is not None and (nota < 0 or nota > 5):
            raise forms.ValidationError("La nota debe estar entre 0 y 5.")
        return nota
