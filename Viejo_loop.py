import numpy as np
import cv2 as cv
import time
from ffpyplayer.player import MediaPlayer
import serial

# Configurar el puerto serial
# Asegurarse de que el puerto COM3 es el correcto para tu dispositivo o cambiarlo según sea necesario
ser = serial.Serial("COM10", 115200)
# Si el puerto no está disponible, dará un error y morirá el programa
# Revisar en el arduino los baud rate y puerto
# Si no se encuentra el puerto, revisar en el administrador de dispositivos de Windows


 # Creo la ventana con nombre
cv.namedWindow("VibroVincha", cv.WINDOW_NORMAL)   
# Y ajusto su tamaño 
 
cv.resizeWindow("VibroVincha", 1280,720)

# Abro el archivo de texto con las lineas de vibra
# Leo todas las lineas de vibra del archivo
file1 = open('data/alfie.txt', 'r')

# Defino el video a reproducir
video = 'data/alfie.mp4'

# Defino el archivo de texto con las lineas de vibra
lineas = file1.readlines()

hora=time.time_ns()
count = 0



# cap = cv.VideoCapture('')
cap = cv.VideoCapture(video)
player = MediaPlayer(video)

if not cap.isOpened():
    print("No se pudo abrir el video")
    exit()
while True:
    # Leo cuadro por cuadro
    ret, frame = cap.read()
    audio_frame, val = player.get_frame()  
  

    # Imprime cada 100 miliseg
    if time.time_ns()-hora>100000000:  
        if count < len(lineas)-1: count += 1 # Evita que se desborde
        # print("Linea {} cruda: {}".format(count, lineas[count]))
        cadena=lineas[count].split(", ")[1].strip('"') + "," + lineas[count].split(", ")[2].strip(';\n\t"')
        print(cadena)
        cadena=cadena+'\n\r'
        ser.write(cadena.encode())
        hora=time.time_ns()

    # Si se leyó correctamente el cuadro ret es True
    if not ret:
        # player.close_player()
        print("Cuadro no recibido (Terminó el video?). Saliendo ...")
        ser.write("0,0,0,0B".encode())        
        break
    # if val == 'eof' or audio_frame is None:
        # img, t = audio_frame
        # print("Fin del Audio")
        # ser.write("0,0,0,0B".encode())
        # break  


    cv.imshow('VibroVincha', frame)
    
    # El valor de tef representa el tiempo en ms entre frames. Ajustar manualmente segun FPS del video y compu
    # Usualmente entre 1 y 40 (en Linux todo es más rápido así que suele ir un numero de 20 o mayor)
    tef=29  # Si el video termina antes que los mensajes seriales, ajustar este valor a un numero mayor y viceversa
    

    if cv.waitKey(tef) == ord('q'): 
        break
 
# Una vez completado todo, release la captura y mato todas las ventanas
cap.release()
cv.destroyAllWindows()