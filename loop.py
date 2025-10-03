import vlc
import time
import serial
import keyboard

# Configuración de videos y sus parámetros
videos_config = [
    {
        'video_path': 'data/alfie_rocas.mp4',
        'txt_path': 'data/alfie_rocas.txt',
        'intervalo': 0.10021  # segundos entre una vibra y la siguiente (ajustar sumando o restando de a 0.00001)
    },
    {
        'video_path': 'data/alfie_playa.mp4',  # Segundo video
        'txt_path': 'data/alfie_playa.txt',   # Archivo de texto para el segundo video
        'intervalo': 0.10021  # segundos entre una vibra y la siguiente (ajustar sumando o restando de a 0.00001)
    }
]

# Indicar el COM del puerto serial a usar para comunicar con la vincha
puerto = "COM10"

# ================== No modificar manualmente dese acá en adelante =========================

# Variable para chequear si el puerto serial está disponible
puerto_serial_disponible = False
ser = None

# Configurar el puerto serial
try:
    ser = serial.Serial(puerto, 115200)
    puerto_serial_disponible = True
    print("✅ Puerto serial conectado correctamente")
except serial.SerialException as e:
    puerto_serial_disponible = False
    print(f"❌ Error al conectar puerto serial COM10: {e}")
    print("⚠️  El programa continuará sin comunicación serial")
except Exception as e:
    puerto_serial_disponible = False
    print(f"❌ Error inesperado con puerto serial: {e}")
    print("⚠️  El programa continuará sin comunicación serial")

def reproducir_video(video_path, txt_path, intervalo_tiempo):
    """
    Reproduce un video con su archivo de texto correspondiente
    
    Argumentos:
        video_path: Ruta al archivo de video
        txt_path: Ruta al archivo de texto con datos de vibración
        intervalo_tiempo: Tiempo en segundos entre cada línea enviada al puerto serial
    """
    print(f"\n=== Reproduciendo: {video_path} ===")
    print(f"Archivo de datos: {txt_path}")
    print(f"Intervalo de tiempo: {intervalo_tiempo}s")
    
    # Abrir y leer el archivo de texto
    with open(txt_path, 'r') as file1:
        lineas = file1.readlines()
    
    # Crear instancia de VLC con parámetros para evitar errores de miniatura
    vlc_args = [
        '--no-video-title-show',     # No mostrar título del video
        '--no-snapshot-preview',     # No mostrar preview de capturas
        '--intf=dummy',              # Interfaz dummy (sin GUI)
        '--quiet',                   # Reducir mensajes de salida
    ]
    
    instance = vlc.Instance(vlc_args)
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    player.set_media(media)
    
    # Configurar para pantalla completa
    player.set_fullscreen(True)
    
    # Reproducir el video
    player.play()
    
    # Esperar un momento para que el video inicie y se configure pantalla completa
    time.sleep(1.0)
    
    # Variables de control
    count = 0

    # Se mantiene mientras el video se reproduce
    while True:
        state = player.get_state()
        if state in [vlc.State.Ended, vlc.State.Error]:
            break
 
        if count < len(lineas)-1: 
            count += 1  # Evita que se desborde

        # Procesar la correspondiente línea del archivo
        cadena = lineas[count].split(", ")[1].strip('"') + "," + lineas[count].split(", ")[2].strip(';\n\t"')
         
        # Enviar por serial solo si el puerto está disponible
        if puerto_serial_disponible and ser is not None:
            try:
                cadena = cadena + '\n\r'
                ser.write(cadena.encode())
            except serial.SerialException as e:
                print(f"⚠️  Error al enviar datos por serial: {e}")
        else: # Si el puerto no está disponible, imprime la cadena por consola
                print(cadena)
        
        time.sleep(intervalo_tiempo) # hace la pausa necesaria para sincronizar vibra con video
    # Detener el reproductor
    player.stop()
    print(f"=== Fin de {video_path} ===\n")



def ejecutar_ciclo_videos():
    """Ejecuta un ciclo completo de todos los videos configurados"""
    print("Iniciando reproducción de videos sucesivos...")
    for i, config in enumerate(videos_config, 1):
        print(f"\n--- Video {i} de {len(videos_config)} ---")
        reproducir_video(config['video_path'], config['txt_path'], config['intervalo'])
        
        # Pausa entre videos (opcional)
        if i < len(videos_config):
            print("Pausa de 2 segundos antes del siguiente video...")
            time.sleep(2)
    
    print("¡Ciclo de reproducción completado!")

def esperar_tecla():
    """Espera la presión de teclas para controlar el programa"""
    print("\n" + "="*60)
    print("CONTROLES:")
    print("- Presiona la BARRA ESPACIADORA para reiniciar el ciclo")
    print("- Presiona la tecla Q para salir del programa")
    print("=" * 60)
    print("⏳ Esperando presión de tecla...")
    
    while True:
        try:
            # Esperar a que se presione una tecla
            event = keyboard.read_event()
            
            # Solo procesar eventos de presión de tecla (no liberación)
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'space':
                    print("\n🔄 ¡Barra espaciadora presionada! Reiniciando ciclo de videos...")
                    time.sleep(0.5)
                    return 'restart'
                elif event.name == 'q':
                    print("\n ¡Tecla Q presionada! Saliendo del programa...")
                    return 'quit'
                else:
                    print(f"⚠️  Tecla '{event.name}' no reconocida. Usa BARRA ESPACIADORA o Q.")
                    
        except KeyboardInterrupt:
            print("\n Programa interrumpido por el usuario.")
            return 'quit'
        except Exception as e:
            print(f"❌ Error al detectar tecla: {e}")
            return 'quit'

# Bucle principal del programa
print("=== REPRODUCTOR DE VIDEOS CON VINCHA VIBRADORA ===")
print("Barra espaciadora para reiniciar | Tecla Q para salir")
print("=" * 60)

try:
    while True:
        # Ejecutar ciclo de videos
        ejecutar_ciclo_videos()
        
        # Esperar comando del usuario mediante detección de teclas
        resultado = esperar_tecla()
        
        if resultado == 'quit':
            break
        elif resultado == 'restart':
            continue  # Reiniciar el bucle
            
except KeyboardInterrupt:
    print("\n Programa terminado por el usuario (Ctrl+C)")
except Exception as e:
    print(f"\n❌ Error inesperado: {e}")
finally:
    # Cerrar puerto serial si está abierto
    if puerto_serial_disponible and ser is not None:
        try:
            ser.close()
            print("🔌 Puerto serial cerrado correctamente")
        except Exception as e:
            print(f"⚠️  Error al cerrar puerto serial: {e}")

print("¡Programa finalizado!")
