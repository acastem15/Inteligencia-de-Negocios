# App - Procesamiento de Reseñas

Esta aplicación permite clasificar una reseña y obtener una probabilidad asociada a la confiabilidad de esta clasificación. A continuación, se presenta el paso a paso para utilizar la aplicación.

## Paso 1

Ingresar a GitHub y copiar la URL del proyecto. Esta es la URL: https://github.com/acastem15/Inteligencia-de-Negocios.git

## Paso 2

Descargar un IDE como VisualStudioCode y clonar el proyecto en su computador de forma local utilizando la opción Git Clone from URL al presionar Ctrl+Shift+P. Además, se debe descargar Docker en el siguiente enlace: https://www.docker.com/products/docker-desktop/

## Paso 3

Crear un ambiente virtual para ejecutar descargar las dependencias de la aplicación. Presionar Ctrl+Shift+P y escribir Create Environment. Seleccionar la opción venv y esperar a que se configure.

## Paso 4

Abrir una terminal usando el menú superior de VisualStudioCode de la siguiente manera:

... --> Terminal --> New Terminal

## Paso 5

Cambiar la ruta que se encuentra en la terminal y ubicarse en la carpeta "Proyecto1". Esto se puede conseguir ejecutando el siguiente comando en la terminal:

`cd Proyecto1`

## Paso 6

Ejecutar el siguiente comando para inicializar la aplicación y su base de datos PostgreSQL utilizando Docker.

`docker-compose up`

## Paso 7

Diríjase a un navegador como Google Chrome y escriba la siguiente dirección:

`localhost:3000`

## Paso 8

Escriba una nueva reseña y presione e botón "Predecir". En pantalla se desplegarán los resultados de la reseña que usted escribió

## Paso 9

Para finalizar el uso de la aplicación, en la terminal de VisualStudioCode ejecute Ctrl+C y la aplicación se detendrá.
