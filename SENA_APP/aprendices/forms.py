from django import forms
from .models import Aprendiz


class AprendizForm(forms.ModelForm):
    class Meta:
        model = Aprendiz
        fields = ['documento_identidad', 'nombre', 'apellido', 'telefono', 'correo', 'fecha_nacimiento', 'ciudad']
        labels = {
            'documento_identidad': 'Documento de Identidad',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'ciudad': 'Ciudad',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_documento_identidad(self):
        documento = self.cleaned_data.get('documento_identidad')
        if documento and not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        # Verificar si el documento ya existe (excepto cuando se está editando)
        if self.instance.pk:  # Si es una edición
            if Aprendiz.objects.exclude(pk=self.instance.pk).filter(documento_identidad=documento).exists():
                raise forms.ValidationError("Ya existe un aprendiz con este documento de identidad.")
        else:  # Si es una creación
            if Aprendiz.objects.filter(documento_identidad=documento).exists():
                raise forms.ValidationError("Ya existe un aprendiz con este documento de identidad.")
        return documento

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono