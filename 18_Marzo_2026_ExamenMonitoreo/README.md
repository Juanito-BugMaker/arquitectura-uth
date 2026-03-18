# Monitoreo de Sistema con Django, Psutil y Docker 🖥️📊

## Presentado por
* Inmer Geraldo Suazo Velasquez - 202020010269

## Descripción del Proyecto
Este proyecto es una aplicación web desarrollada en **Django** que utiliza la librería **psutil** para extraer métricas del hardware (CPU, RAM, Disco) en tiempo real. La aplicación presenta estos datos de manera gráfica y amigable usando Bootstrap, y cuenta con recarga automática mediante JavaScript. Todo el entorno está contenerizado usando **Docker**.

## Instrucciones de Instalación Local y Ejecución (Docker)

1. Clonar este repositorio.
2. Asegúrate de tener instalado [Docker Desktop](https://www.docker.com/products/docker-desktop/).
3. Abre una terminal en la carpeta raíz del proyecto.
4. Ejecuta el siguiente comando para construir y levantar el contenedor:
   ```bash
   docker-compose up --build