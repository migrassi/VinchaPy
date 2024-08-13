# VinchaPy
Recursos y pruebas para la Vincha Vibradora. Requiere instalar el OpenCV para Python: [Install OpenCV-Python](https://docs.opencv.org/4.x/da/df6/tutorial_py_table_of_contents_setup.html)

## Contenidos

## VideoTest.py 
Pequeño script en Python que carga y muestra un video, sin sonido, al tiempo que envía por el puerto serie o Bluetooth, cada  100 milisegundos una linea de control a los motovibradores externos, que lee de un archivo de texto.
El video y el archivo deben estar en la subcarpeta "data" y el formato de cada línea de texto debe ser exactamente la que fue fue generada originalmente.

Ejemplo: 

     0, "0,0, 126,126,0B"; 

**Prestar especial atención a los espacios!!** Hay uno después de la primera coma y otro después de la tercera. 

## ImageTest.py
Script de prueba para verificar que OpenCV-Python está correctamente instalado. Muestra una ventana con una imagen jpg que está en la sub-carpeta "data"