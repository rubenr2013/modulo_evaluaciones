from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Evaluacion
from .forms import EvaluacionForm


def lista_evaluaciones(request):
    evaluaciones = Evaluacion.objects.all().order_by('-fecha')
    context = {
        'evaluaciones': evaluaciones,
        'total_evaluaciones': evaluaciones.count(),
    }
    return render(request, 'evaluaciones/lista_evaluaciones.html', context)

class EvaluacionFormView(generic.FormView):
    template_name = 'evaluaciones/agregar_evaluacion.html'
    form_class = EvaluacionForm
    success_url = reverse_lazy('evaluaciones:lista_evaluaciones')

    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        messages.success(self.request, f'La evaluación para {form.instance.aprendiz} ha sido registrada exitosamente.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)

