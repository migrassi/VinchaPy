import numpy as np
import cv2 as cv
import time
from ffpyplayer.player import MediaPlayer

 # Basado en el ejemplo de https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
 
 # Leo todas las lineas de vibra del archivo
file1 = open('data/lineas_01.txt', 'r')

# video = 'data/baldosas.mp4'
video = 'data/1280x720_5mb.mp4'

lineas = file1.readlines()

hora=time.time_ns()
count = 0

# Creo la ventana con nombre
cv.namedWindow("VibroVincha", cv.WINDOW_NORMAL)   
# Y ajusto su tamaño 
# cv.resizeWindow("VibroVincha", 1024,540) 
cv.resizeWindow("VibroVincha", 1280,720)

# cap = cv.VideoCapture('')
cap = cv.VideoCapture(video)
player = MediaPlayer(video)

if not cap.isOpened():
    print("No se pudo abrir el video")
    exit()
while True:
    # Leo cuadro por cuadro
    ret, frame = cap.read()
    # audio_frame, val = player.get_frame()

    # Imprime cada 100 miliseg
    if time.time_ns()-hora>100000000:  
        if count < len(lineas)-1: count += 1 # Evita que se desborde
        print("Linea {} cruda: {}".format(count, lineas[count]))
        # print(lineas[count].split(", ")[1] + "," + lineas[count].split(", ")[2].strip(';\n\t'))
        hora=time.time_ns()

    # Si se leyó correctamente el cuadro ret es True
    if not ret:
        print("Cuadro no recibido (Terminó el video?). Saliendo ...")
        break

    # Acá puedo operar sobre el frame
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Mostrar el frame
    #cv.imshow('frame', gray)
    #cv.imshow('frame', frame)

    #if val != 'eof' and audio_frame is not None:
        #audio
        #img, t = audio_frame
    cv.imshow('VibroVincha', frame)
    
    # El valor de tef representa el tiempo en ms entre frames. Ajustar manualmente segun FPS del video y compu
    # Usualmente entre 1 y 40 (en Linux todo es más rápido así que suele ir un numero de 20 o mayor)
    tef=30

    if cv.waitKey(tef) == ord('q'): 
        break
 
# Una vez completado todo, release la captura y mato todas las ventanas
cap.release()
cv.destroyAllWindows()