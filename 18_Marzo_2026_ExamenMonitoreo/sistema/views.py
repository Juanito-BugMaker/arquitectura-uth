# Inmer Geraldo Suazo Velasquez - 202020010269

from django.shortcuts import render
# Create your views here.
import psutil
import platform

def index(request):
    # Diccionario para enviar a la plantilla HTML
    context = {}
    
    try:
        # 1. Información del Sistema Operativo y CPU
        context['os_info'] = f"{platform.system()} {platform.release()}"
        context['cpu_cores'] = psutil.cpu_count(logical=True)
        # interval=0.1 evita que la petición web se quede "colgada" esperando 1 segundo entero
        context['cpu_percent'] = psutil.cpu_percent(interval=0.1)

        # 2. Información de la RAM (Convertimos bytes a GB)
        ram = psutil.virtual_memory()
        context['ram_total_gb'] = round(ram.total / (1024**3), 2)
        context['ram_used_gb'] = round(ram.used / (1024**3), 2)
        context['ram_percent'] = ram.percent

        # 3. Información del Disco Duro ('/' es la raíz en Linux/Mac, en Windows igual funciona o usar 'C:\\')
        disco = psutil.disk_usage('/')
        context['disk_total_gb'] = round(disco.total / (1024**3), 2)
        context['disk_used_gb'] = round(disco.used / (1024**3), 2)
        context['disk_free_gb'] = round(disco.free / (1024**3), 2)
        context['disk_percent'] = disco.percent

        context['error'] = False # Si todo sale bien, no hay error

    except Exception as e:
        # MANEJO DE ERRORES
        context['error'] = True
        context['mensaje_error'] = f"Error al obtener datos del sistema: {str(e)}"

    return render(request, 'sistema/index.html', context)