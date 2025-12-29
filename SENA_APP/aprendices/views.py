from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Aprendiz, Curso
from instructores.models import Instructor
from programas.models import Programa
from .forms import AprendizForm


def aprendices(request):
    lista_aprendices = Aprendiz.objects.all().order_by('apellido', 'nombre')

    context = {
        'lista_aprendices': lista_aprendices,
        'total_aprendices': lista_aprendices.count(),
    }
    return render(request, 'lista_aprendices.html', context)


def inicio(request):
    # Estadísticas generales
    total_aprendices = Aprendiz.objects.count()
    total_instructores = Instructor.objects.count()
    total_programas = Programa.objects.count()
    total_cursos = Curso.objects.count()
    cursos_activos = Curso.objects.filter(estado__in=['INI', 'EJE']).count()

    context = {
        'total_aprendices': total_aprendices,
        'total_cursos': total_cursos,
        'cursos_activos': cursos_activos,
        'total_instructores': total_instructores,
        'total_programas': total_programas,
    }

    return render(request, 'inicio.html', context)


def lista_cursos(request):
    cursos = Curso.objects.all().order_by('-fecha_inicio')

    context = {
        'lista_cursos': cursos,
        'total_cursos': cursos.count(),
        'titulo': 'Lista de Cursos'
    }

    return render(request, 'lista_cursos.html', context)


def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()

    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }

    return render(request, 'detalle_curso.html', context)


def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id)

    context = {
        'aprendiz': aprendiz,
    }

    return render(request, 'detalle_aprendiz.html', context)


class AprendizFormView(generic.CreateView):
    template_name = "agregar_aprendiz.html"
    form_class = AprendizForm
    success_url = reverse_lazy('aprendices:lista_aprendices')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrija los errores en el formulario.')
        return super().form_invalid(form)
    