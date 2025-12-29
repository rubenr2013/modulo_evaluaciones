# Instrucciones para Aplicar los Cambios

## ⚠️ IMPORTANTE: Debes ejecutar estos comandos para aplicar los cambios

Después de todas las correcciones realizadas, necesitas ejecutar los siguientes comandos:

## 1. Instalar dependencias

```bash
cd SENA_APP
pip install -r requirements.txt
```

## 2. Crear migraciones para los cambios en los modelos

Los siguientes modelos fueron modificados:
- `Aprendiz`: Se agregó `blank=True` a campos opcionales
- `Curso`: Se agregó validación de fechas (clean method)
- `Evaluacion`: Se agregó campo `curso`, validadores de nota, índices

```bash
python manage.py makemigrations
```

## 3. Aplicar las migraciones

```bash
python manage.py migrate
```

## 4. Verificar que todo funcione

```bash
python manage.py check
```

## 5. (Opcional) Crear un superusuario si no tienes uno

```bash
python manage.py createsuperuser
```

## 6. Ejecutar el servidor

```bash
python manage.py runserver
```

---

## Resumen de Cambios Realizados

### ✅ Errores Críticos Corregidos

1. **Error de sintaxis en evaluaciones/views.py** - Línea 19: `'total_e evaluaciones'` → `'total_evaluaciones'`
2. **Imports duplicados eliminados** en evaluaciones/views.py
3. **SECRET_KEY movida a .env** - Mayor seguridad

### ✅ Mejoras Importantes

4. **AprendizForm refactorizado** - Ahora usa `ModelForm` en lugar de `Form`
5. **success_url corregido** - Usa `reverse_lazy` en lugar de rutas relativas
6. **Vistas modernizadas** - Reemplazadas por `render()` en lugar de `loader.get_template()`
7. **Modelo Evaluacion mejorado**:
   - Agregado campo `curso` (ForeignKey)
   - Validadores de nota (0-5) a nivel de modelo
   - Validación que verifica que el aprendiz esté inscrito en el curso
   - Índices de base de datos agregados
8. **Modelo Curso validado** - Ahora valida que fecha_fin > fecha_inicio
9. **Campos opcionales corregidos** - Agregado `blank=True` donde corresponde

### ✅ Configuración Regional

10. **Idioma y zona horaria** - Cambiado a español colombiano (es-co) y America/Bogota

### ✅ Archivos Creados

- `.env` - Variables de entorno
- `.env.example` - Plantilla de variables de entorno
- `.gitignore` - Para no subir archivos sensibles a git
- `requirements.txt` - Dependencias del proyecto
- Este archivo de instrucciones

---

## Notas Adicionales

### Sobre el campo curso en Evaluacion

El modelo `Evaluacion` ahora tiene un campo opcional `curso`. Esto permite:
- Asociar evaluaciones a cursos específicos
- Validar que el aprendiz esté inscrito en el curso
- Tener mejor trazabilidad de las evaluaciones

Si tienes evaluaciones existentes en la base de datos, el campo `curso` será `NULL` para esas evaluaciones antiguas (lo cual está permitido porque es `null=True, blank=True`).

### Sobre las validaciones

Ahora los modelos tienen validaciones más robustas:
- Las notas deben estar entre 0 y 5
- Las fechas de fin deben ser posteriores a las fechas de inicio
- Los aprendices deben estar inscritos en el curso para tener evaluaciones

Estas validaciones se ejecutan tanto en formularios como en el modelo.
