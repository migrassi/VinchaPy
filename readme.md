# VinchaPy

Sistema de reproducción de videos sincronizados con vincha vibradora.

## Instalación y Configuración

### Requisitos previos
- Python 3.8 o superior
- VLC Media Player instalado en el sistema
- Puerto serial disponible (COM10 por defecto)

### Instalación 

 Aunque hayas clonado todo el repositorio, **es necesario instalar las dependencias de Python**, ya que las librerías no se incluyen en el repositorio por razones de seguridad y tamaño. Los pasos serían:

1. **Clonar el repositorio ejecutando, en el directorio que quieras:**
   
   ```bash
   git clone https://github.com/migrassi/VinchaPy.git
   cd VinchaPy
   ```

  Aunque hayas clonado el repositorio, **SIEPRE tenes que crear vos el entorno virtual** porque los entornos virtuales tampoco se incluyen en los repositorios.

2. **Crear el entorno virtual:**
     
    ```bash
    python -m venv .venv                # CREAR el entorno virtual
   ```

3. **Instalar las dependencias sin activar el entorno virtual**

   ```bash
     .venv\Scripts\pip.exe install python-vlc pyserial keyboard

   ```

4. **Ejecutar el programa sin activar el entorno virtual**   
   ```bash
     .venv\Scripts\python.exe loop.py
     
   ```

### Estructura de archivos requerida:
```
VinchaPy/
├── loop.py
├── data/
│   ├── alfie_rocas.mp4
│   ├── alfie_rocas.txt
│   ├── alfie_playa.mp4
│   └── alfie_playa.txt
```

**Verificar que VLC esté instalado** en tu sistema operativo (no la librería Python, sino el programa VLC Media Player)

## loop.py - Este es el Reproductor

**`loop.py`** es el programa principal actualizado que permite reproducir videos con sincronización de vibración usando VLC como motor de reproducción.

### Características principales:
- ✅ **Reproducción en pantalla completa** con VLC
- ✅ **Comunicación serial** con la vincha vibradora
- ✅ **Control por teclado** en tiempo real
- ✅ **Ciclo automático** de múltiples videos
- ✅ **Manejo robusto de errores**

**Ejecutar el programa sin activar el entorno virtual**   
   ```bash
     .venv\Scripts\python.exe loop.py
     
   ```

### Control de teclado:
- **BARRA ESPACIADORA**: Reinicia el ciclo de videos
- **Tecla Q**: Sale del programa
- **Ctrl+C**: Salida de emergencia

### Configuración:

1. **Editar la configuración de videos** en `loop.py`:
   ```python
   videos_config = [
       {
           'video_path': 'data/alfie_rocas.mp4',
           'txt_path': 'data/alfie_rocas.txt',
           'intervalo': 0.10021  # segundos entre vibraciones
       },
       {
           'video_path': 'data/alfie_playa.mp4',
           'txt_path': 'data/alfie_playa.txt',
           'intervalo': 0.10021
       }
   ]
   ```

2. **Configurar el puerto serial** (línea 17):
   ```python
   puerto = "COM10"  # Cambiar según tu sistema
   ```

### Solución de problemas:
- **Error de puerto serial**: El programa continúa sin comunicación serial, imprime los comandos por consola
- **Videos no encontrados**: Verificar rutas en `videos_config`
- **Error de VLC**: Asegurar que VLC esté instalado en el sistema

---

## 📚 Información de referencia (versiones anteriores)

___
A partir de acá información desactualizada. La mantenemos como referencia
___


Recursos y pruebas para la Vincha Vibradora. Requiere  OpenCV para Python, que se instala con el comando:

     pip install opencv-python

Para poder reproducir también el audio asociado al video utilizado, es necesario instalar también las librerías FFmpeg mediante su binding `ffplayer` ejecutando el comando:  

     pip install ffpyplayer

Obviamente, para los comandos pip debe disponerse previamente de Python instalado en la computadora. 

Si no se dispone de Python, es muy simple de [instalar desde la Microsoft Store](ms-windows-store://pdp?hl=es-es&gl=ar&referrer=storeforweb&productid=9pjpw5ldxlz5&ocid=storeweb-pdp-open-cta) y luego ya podrá ejecutarse el comando anterior desde una ventana cmd.

Para instalar Python en otros sistemas operativos ver [Python for Linux/UNIX](https://www.python.org/downloads/source/), [Python for macOS](https://www.python.org/downloads/macos/), [Python for others platforms](https://www.python.org/download/other/).

 
## Programas y archivos incluidos en este repositorio

## VideoTest.py 
Pequeño script en Python que carga y muestra un video, al tiempo que envía por el puerto serie o Bluetooth, cada  100 milisegundos, una linea de control a los motovibradores externos, que lee de un archivo de texto auxiliar.
El video y el archivo auxiliar deben estar en la subcarpeta "data" y el formato de cada línea de texto debe ser exactamente el mismo formato que tiene la línea generada originalmente.

Ejemplo: 

     0, "0,0, 126,126,0B"; 

**Prestar especial atención a los espacios!!** Hay uno después de la primera coma y otro después de la tercera. 

Al ejecutarlo hay que ajustar el valor de la variable tef, para que el video dure el tiempo normal y finalice en forma sincronizada con el sonido y el envío de las líneas de control de motovibradores. El valor de tef representa el tiempo en ms que se debe pausar entre frames, de acuerdo a la demora en cargarlos, que a su vez depende de los  FPS del video, así como de la compu y SO utilizados. Usualmente va un valor entre 1 y 40 (en Linux todo es más rápido así que suele ir un numero de 20 o mayor). No debe exceder los 100 milisegundos para que no afecte la secuencia de los comandos de vibración.

## ImageTest.py
Script de prueba para verificar que OpenCV-Python está correctamente instalado. Muestra una ventana con una imagen jpg que está en la sub-carpeta "data".

## audioTest.py
Script de prueba de sonido. Sirve para verificar que `ffpyplayer` y las librerías FFmpeg funcionan correctamente. No termina automáticamente. Debe interrumpirse por consola con Ctrl-C o Ctrl-X, etc.

## 1280x720_5mb.mp4 
Archivo de video para pruebas. Dura 30" e incluye audio.

## baldosas.mp4
Archivo de video para pruebas. Dura 30" NO TIENE audio.

## Lineas_01.txt
Archivo de texto con las líneas de comandos suficientes para 30" si se envían a razón de una cada 100 milisegundos.

## starry_night.jpg
Archivo de imagen para pruebas estáticas. 