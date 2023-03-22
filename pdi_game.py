#--------------------------------------------------------------------------
#------- Juego de PDI------------------------------------------------------
#------- Por: Santiago Santa Agudelo    santiago.santa@udea.edu.co --------
#-------      Juan Gabriel Orozco Orozco    jgabriel.orozco@udea.edu.co ---
#-------      Estudiantes de Ingeniería Electrónica -----------------------
#------- Curso Básico de Procesamiento de Imágenes ------------------------
#------- Marzo de 2023-----------------------------------------------------
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#------- Importación de Librerías -----------------------------------------
#--------------------------------------------------------------------------

import numpy as np  # Librería para el manejo de vectores y matrices multidimensionales.
import cv2          # Librería para el manejo de imagenes
import keyboard     # Librería para la ingestación de teclas

#--------------------------------------------------------------------------
#------- Seleccionar la cámara predeterminada -----------------------------
#--------------------------------------------------------------------------


cap = cv2.VideoCapture(0) # Selecciona la cámara predeterminada

#--------------------------------------------------------------------------
#------- Definición de las coordenadas para los rectángulos ---------------
#--------------------------------------------------------------------------

# Figuras de 480x640 pixeles
height = 480
width = 640

# Coordenadas de rectángulos
w = int(width/4)    # Anchura de cada rectángulo
h = int(height/4)   # Altura de cada rectángulo
x1 = int(w*0)       # Coordenada en X del rectángulo izquierdo
x2 = int(w*1.5)     # Coordenada en X del rectángulo de arriba
x3 = int(w*3)       # Coordenada en X del rectángulo derecho
y1 = int(h*0)       # Coordenada en Y del rectángulo de arriba
y2 = int(h*1.5)     # Coordenada en Y de los rectángulos izquierdo y derecho

#--------------------------------------------------------------------------
#------- Valores HSV para filtrar el color de la piel ---------------------
#--------------------------------------------------------------------------

# Mascara para el color de piel
lower_hsv = np.array([0, 29, 0])        # El valor bajo de H, S y V es 0, 29 y 0 respectivamente
higher_hsv = np.array([52, 186, 255])   # El valor alto de H, S y V es 0, 29 y 0 respectivamente

#--------------------------------------------------------------------------
#------- Ciclo donde se procesa un frame cada 100ms -----------------------
#--------------------------------------------------------------------------

while True:

    #--------------------------------------------------------------------------
    #------- Captura y reflejo del frame --------------------------------------
    #--------------------------------------------------------------------------

    ret, frame = cap.read()     # Captura del Frame
    frame = cv2.flip(frame, 1)  # Se refleja el frame

    # Si no se puede capturar un fotograma, salir del bucle
    if not ret:
        break

    #--------------------------------------------------------------------------
    #------- Dibujar los rectángulos izquierdo, arriba y derecho --------------
    #--------------------------------------------------------------------------

    # Dibuja los rectángulos con borde negro de 2 píxeles de ancho
    cv2.rectangle(frame, (x1, y2), (x1 + w, y2 + h), 0, thickness=2) # Izquierda
    cv2.rectangle(frame, (x2, y1), (x2 + w, y1 + h), 0, thickness=2) # Arriba
    cv2.rectangle(frame, (x3, y2), (x3 + w, y2 + h), 0, thickness=2) # Derecha

    # Muestra el fotograma capturado
    cv2.imshow('Capturando video', frame)

    #--------------------------------------------------------------------------
    #------- Capturar los rectángulos izquierdo, arriba y derecho -------------
    #--------------------------------------------------------------------------
    
    izquierda_frame = frame[y2:y2+h,x1:x1+w]    # Izquierda
    arriba_frame = frame[y1:y1+h,x2:x2+w]       # Arriba
    derecha_frame = frame[y2:y2+h,x3:x3+w]      # Derecha

    #--------------------------------------------------------------------------
    #------- Llevar los rectángulos al formato HSV y filtar el color piel -----
    #--------------------------------------------------------------------------

    # Pasando a HSV
    izquierda_hsv = cv2.cvtColor(izquierda_frame, cv2.COLOR_BGR2HSV)    # Izquierda
    arriba_hsv = cv2.cvtColor(arriba_frame, cv2.COLOR_BGR2HSV)          # Arriba
    derecha_hsv = cv2.cvtColor(derecha_frame, cv2.COLOR_BGR2HSV)        # Derecha

    # Filtrando el color piel -> se obtiene pixel blanco si detecta el color piel
    # y pixel negro si hay ausencia de color piel
    izquierda_mask = cv2.inRange(izquierda_hsv, lower_hsv, higher_hsv)  # Izquierda
    arriba_mask = cv2.inRange(arriba_hsv, lower_hsv, higher_hsv)        # Arriba
    derecha_mask = cv2.inRange(derecha_hsv, lower_hsv, higher_hsv)      # Derecha

    #Mostrar fragmentos procesados - Debug Only
    #cv2.imshow('Capturando izquierda', izquierda_mask)
    #cv2.imshow('Capturando arriba', arriba_mask)
    #cv2.imshow('Capturando derecha', derecha_mask)

    #--------------------------------------------------------------------------
    #------- Detección de color piel en los rectángulos -----------------------
    #--------------------------------------------------------------------------

    # Promedios para detección del color piel (promedio de los pixeles blancos)
    izquierda_mean = int(np.mean(izquierda_mask))
    arriba_mean = int(np.mean(arriba_mask))
    derecha_mean = int(np.mean(derecha_mask))
    
    #Umbrales de detección
    if izquierda_mean > 50:     # Si en el recángulo de la izquierda el promedio de pixeles blancos es mayor
        print("Izquierda")      # a 50, se presiona la tecla 'a'
        keyboard.press('a')
    else:
        keyboard.release('a')   # De lo contrario libere la tecla 'a'
    if arriba_mean > 50:        # Si en el recángulo de arriba el promedio de pixeles blancos es mayor
        print("Arriba")         # a 50, se presiona la tecla 'w'
        keyboard.press('w')
    else:
        keyboard.release('w')   # De lo contrario libere la tecla 'w'
    if derecha_mean > 50:       # Si en el recángulo de la derecha el promedio de pixeles blancos es mayor
        print("Derecha")        # a 50, se presiona la tecla 'd'
        keyboard.press('d')
    else:
        keyboard.release('d')   # De lo contrario libere la tecla 'd'

    #--------------------------------------------------------------------------
    #------- Condición finalización del ciclo y espera de 100ms ---------------
    #--------------------------------------------------------------------------

    # Espera 100 milisegundos y si el usuario presiona la tecla 'q' se cierra el programa
    if cv2.waitKey(100) == ord('q'):
        break
    
# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()

#--------------------------------------------------------------------------
#---------------------------  FIN DEL PROGRAMA ----------------------------
#--------------------------------------------------------------------------