#Importar librerías
import numpy as np
import cv2
#import keyboard

# keyboard.press('a')
# keyboard.release('a')

# Figuras de 480x640 pixeles
# Selecciona la cámara predeterminada
cap = cv2.VideoCapture(0)

# Altura y ancho de frame
height = 480
width = 640

# Coordenadas de rectángulos
w = int(width/4)
h = int(height/4)
x1 = int(w*0)
x2 = int(w*1.5)
x3 = int(w*3)
y1 = int(h*0)
y2 = int(h*1.5)

while True:
    # CAPTURA FOTOGRAMA 1
    
    ret, frame1 = cap.read()
    # Refleja el fotograma
    frame1 = cv2.flip(frame1, 1)

    # Si no se puede capturar un fotograma, salir del bucle
    if not ret:
        break

    # Convierte la imagen a escala de grises
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    # Dibuja los rectángulos con borde negro de 2 píxeles de ancho
    cv2.rectangle(frame1_gray, (x1, y2), (x1 + w, y2 + h), 0, thickness=2) # Izquierda
    # cv2.rectangle(frame1_gray, (x1, y1), (x1 + w, y1 + h), 0, thickness=2) # Arriba-Izquierda
    cv2.rectangle(frame1_gray, (x2, y1), (x2 + w, y1 + h), 0, thickness=2) # Arriba
    # cv2.rectangle(frame1_gray, (x3, y1), (x3 + w, y1 + h), 0, thickness=2) # Arriba-Derecha
    cv2.rectangle(frame1_gray, (x3, y2), (x3 + w, y2 + h), 0, thickness=2) # Derecha

    # Muestra el fotograma capturado
    cv2.imshow('Capturando video', frame1_gray)
    
    izquierda_frame1 = frame1_gray[y2:y2+h,x1:x1+w]
    # cv2.imshow('Capturando izquierda', izquierda_frame1)
    arriba_frame1 = frame1_gray[y1:y1+h,x2:x2+w]
    # cv2.imshow('Capturando arriba', arriba_frame1)
    derecha_frame1 = frame1_gray[y2:y2+h,x3:x3+w]
    # cv2.imshow('Capturando derecha', derecha_frame1)

    # Espera 100 milisegundos y espera a que el usuario presione la tecla 'q' para salir
    cv2.waitKey(100)
    
    # CAPTURA FOTOGRAMA 2
    
    ret, frame2 = cap.read()
    # Refleja el fotograma
    frame2 = cv2.flip(frame2, 1)

    # Si no se puede capturar un fotograma, salir del bucle
    if not ret:
        break

    # Convierte la imagen a escala de grises
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Dibuja los rectángulos con borde negro de 2 píxeles de ancho
    cv2.rectangle(frame2_gray, (x1, y2), (x1 + w, y2 + h), 0, thickness=2) # Izquierda
    # cv2.rectangle(frame2_gray, (x1, y1), (x1 + w, y1 + h), 0, thickness=2) # Arriba-Izquierda
    cv2.rectangle(frame2_gray, (x2, y1), (x2 + w, y1 + h), 0, thickness=2) # Arriba
    # cv2.rectangle(frame2_gray, (x3, y1), (x3 + w, y1 + h), 0, thickness=2) # Arriba-Derecha
    cv2.rectangle(frame2_gray, (x3, y2), (x3 + w, y2 + h), 0, thickness=2) # Derecha
    
    izquierda_frame2 = frame2_gray[y2:y2+h,x1:x1+w]
    # cv2.imshow('Capturando izquierda', izquierda_frame2)
    arriba_frame2 = frame2_gray[y1:y1+h,x2:x2+w]
    # cv2.imshow('Capturando arriba', arriba_frame2)
    derecha_frame2 = frame2_gray[y2:y2+h,x3:x3+w]
    # cv2.imshow('Capturando derecha', derecha_frame2)

    # Espera 100 milisegundos y espera a que el usuario presione la tecla 'q' para salir
    if cv2.waitKey(100) == ord('q'):
        break
    
    # LOGICA CON LOS FRAMES 1 Y 2
    
    

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()