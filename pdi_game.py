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

# Mascara para el color de piel
lower_hsv = np.array([18, 0, 0])
higher_hsv = np.array([179, 255, 255])

while True:
    # CAPTURA FOTOGRAMA 1
    
    ret, frame = cap.read()
    # Refleja el fotograma
    frame = cv2.flip(frame, 1)

    # Si no se puede capturar un fotograma, salir del bucle
    if not ret:
        break

    # Dibuja los rectángulos con borde negro de 2 píxeles de ancho
    cv2.rectangle(frame, (x1, y2), (x1 + w, y2 + h), 0, thickness=2) # Izquierda
    # cv2.rectangle(frame, (x1, y1), (x1 + w, y1 + h), 0, thickness=2) # Arriba-Izquierda
    cv2.rectangle(frame, (x2, y1), (x2 + w, y1 + h), 0, thickness=2) # Arriba
    # cv2.rectangle(frame, (x3, y1), (x3 + w, y1 + h), 0, thickness=2) # Arriba-Derecha
    cv2.rectangle(frame, (x3, y2), (x3 + w, y2 + h), 0, thickness=2) # Derecha

    # Muestra el fotograma capturado
    cv2.imshow('Capturando video', frame)
    
    izquierda_frame = frame[y2:y2+h,x1:x1+w]
    #cv2.imshow('Capturando izquierda', izquierda_frame)
    arriba_frame = frame[y1:y1+h,x2:x2+w]
    #cv2.imshow('Capturando arriba', arriba_frame)
    derecha_frame = frame[y2:y2+h,x3:x3+w]
    #cv2.imshow('Capturando derecha', derecha_frame)

    #Pasando a HSV
    izquierda_hsv = cv2.cvtColor(izquierda_frame, cv2.COLOR_BGR2HSV)
    arriba_hsv = cv2.cvtColor(arriba_frame, cv2.COLOR_BGR2HSV)
    derecha_hsv = cv2.cvtColor(derecha_frame, cv2.COLOR_BGR2HSV)

    #Aplicando máscara de piel
    izquierda_mask = cv2.inRange(izquierda_hsv, lower_hsv, higher_hsv)
    arriba_mask = cv2.inRange(arriba_hsv, lower_hsv, higher_hsv)
    derecha_mask = cv2.inRange(derecha_hsv, lower_hsv, higher_hsv)

    #Mostrar fragmentos procesados
    cv2.imshow('Capturando izquierda', izquierda_mask)
    cv2.imshow('Capturando arriba', arriba_mask)
    cv2.imshow('Capturando derecha', derecha_mask)

    # Espera 100 milisegundos y espera a que el usuario presione la tecla 'q' para salir
    if cv2.waitKey(100) == ord('q'):
        break

    
# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()