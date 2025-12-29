# 🎓 SENA APP - Sistema de Gestión de Aprendices

Sistema desarrollado con Django para gestionar aprendices, cursos, instructores, programas y evaluaciones del SENA.

## ✅ Estado del Proyecto

**Todas las correcciones han sido aplicadas y las migraciones ejecutadas exitosamente.**

---

## 🚀 Inicio Rápido

### 1. Instalar dependencias (si aún no lo has hecho)

```bash
pip install -r requirements.txt
```

### 2. Ejecutar el servidor

```bash
python manage.py runserver
```

### 3. Acceder al sistema

- **Aplicación:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

---

## 📂 Estructura del Proyecto

```
SENA_APP/
├── aprendices/          # App de aprendices y cursos
├── instructores/        # App de instructores
├── programas/           # App de programas de formación
├── evaluaciones/        # App de evaluaciones
├── SENA_APP/           # Configuración del proyecto
├── .env                # Variables de entorno (NO subir a git)
├── .env.example        # Plantilla de variables
├── .gitignore          # Archivos ignorados por git
├── requirements.txt    # Dependencias Python
└── db.sqlite3          # Base de datos SQLite
```

---

## 🔧 Configuración

### Variables de Entorno

El proyecto usa un archivo `.env` para configuración sensible:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
LANGUAGE_CODE=es-co
TIME_ZONE=America/Bogota
```

---

## 📊 Modelos Principales

### Aprendiz
- Documento de identidad (único)
- Información personal (nombre, apellido, fecha de nacimiento)
- Información de contacto (teléfono, correo, ciudad)

### Curso
- Código único
- Programa de formación asociado
- Instructor coordinador
- Fechas de inicio y fin (con validación)
- Cupos y estado del curso
- Relación many-to-many con aprendices e instructores

### Evaluación
- Aprendiz evaluado
- Curso asociado (opcional)
- Tipo (Teórica, Práctica, Proyecto)
- Nota (0-5) con validación
- Estado (Pendiente, Realizada, Corregida)
- Validación: aprendiz debe estar inscrito en el curso

---

## ✨ Características

### Validaciones Implementadas

1. **Curso:** Fecha de finalización debe ser posterior a fecha de inicio
2. **Evaluación:** Nota entre 0 y 5
3. **Evaluación:** Aprendiz debe estar inscrito en el curso
4. **Aprendiz:** Documento de identidad único
5. **Formularios:** Validación de campos numéricos

### Mejoras de Seguridad

- SECRET_KEY en variables de entorno
- .gitignore configurado
- DEBUG controlado por variables de entorno

### Optimizaciones

- Índices de base de datos en campos consultados frecuentemente
- Uso de `select_related` y `prefetch_related` (implementable)
- Validaciones a nivel de modelo y formulario

---

## 🎨 Interfaz de Administración

El panel de admin está completamente configurado con:

- **List display** personalizado para todos los modelos
- **Filtros** por campos relevantes
- **Búsqueda** configurada
- **Fieldsets** para organizar formularios
- **Inlines** para relaciones (Curso con Aprendices e Instructores)
- **List editable** para edición rápida

---

## 📝 Comandos Útiles

### Crear un superusuario
```bash
python manage.py createsuperuser
```

### Crear migraciones
```bash
python manage.py makemigrations
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Verificar el proyecto
```bash
python manage.py check
```

### Abrir shell de Django
```bash
python manage.py shell
```

---

## 🐛 Problemas Resueltos

Ver el archivo [CAMBIOS_REALIZADOS.md](./CAMBIOS_REALIZADOS.md) para un listado completo de:
- ✅ 3 errores críticos corregidos
- ✅ 7 problemas importantes solucionados
- ✅ 6 mejoras adicionales implementadas
- ✅ 22 mejoras totales aplicadas

---

## 📖 Documentación Adicional

- [CAMBIOS_REALIZADOS.md](./CAMBIOS_REALIZADOS.md) - Detalle completo de todas las correcciones
- [INSTRUCCIONES_MIGRACION.md](./INSTRUCCIONES_MIGRACION.md) - Guía de migraciones

---

## 🤝 Contribuir

1. Crear una rama para tu feature
2. Hacer commit de tus cambios
3. Ejecutar `python manage.py check` para verificar
4. Crear un pull request

---

## 📄 Licencia

Proyecto educativo del SENA.

---

## 👥 Contacto

Para soporte o preguntas sobre el proyecto, contactar al equipo de desarrollo.

---

**Última actualización:** 29 de diciembre de 2025
**Estado:** ✅ Producción lista (desarrollo)
**Django Version:** 5.2.4
