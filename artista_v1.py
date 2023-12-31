import funciones_auxiliares
import random
import time
import datetime
import numpy as np
import cv2 as cv
import cv2 as cv_i
from deepface import DeepFace




# matriz dinámica de asociación de OPIS con estado de ánimo
# la primera fila es la cabecera y son los estados de ánimos del sistema (números)
# las filas siguientes son las opis que corresponden (numero-letras), una columna serían todas las OPIS asociadas al estado de ánimo de la primera fila de esa columna
asociacion = np.array ([[1,2,3,4,5],["fusiona_2_img","fusiona_varias_imgs","musica_amplitud_a_color","func_cos_a_pix","func_log_a_pix"], ["func_sin_a_pix","hebb_RGB_ind","hebb_RGB_per_pixel","recorta_nxm_flipH","recorta_nxm_flipV"], ["figura_collage","difuminado_gaussiano_random","difuminado_gaussiano_full","apagado_pixel","efecto_zoom"]])

#inicializo las imagenes
height = 640
width = 640
imagen_actual= np.zeros((height,width,3), np.uint8)
imagen_vieja= imagen_actual

# esto se repite cada 10s
while (1):
    #guardo imagen_vieja para hacer transicion con la nueva imagen
    imagen_vieja = imagen_actual
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("No se puede acceder a la cámara")
        exit()
    while True:
     # Capture frame-by-frame
        ret, frame = cap.read()
        # si frame is read correctly ret is True
        if not ret:
            print("No se recibe video. Saliendo...")
            break
        # sistema difuso selecciona el estado de animo actual del observador
        resultFace = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        info = [[resultFace[0]['dominant_emotion']]]

        # sistema asimila el estado del animo del observador cambiando ESTADO DE ANIMO DEL SISTEMA
        if info == [['neutral']]:
            # When b is pressed videoChange is 1
            estado_animo_sistema = 0
            break
        if info == [['happy']]:
            # When b is pressed videoChange is 1
            style_name = "yellow"
            estado_animo_sistema = 1
            break
        if info == [['sad']]:
            # When b is pressed videoChange is 1
            style_name = "blue"
            estado_animo_sistema = 2
            break
        if info == [['surprise']]:
            # When b is pressed videoChange is 1
            style_name = "white"
            estado_animo_sistema = 3
            break
        if info == [['angry']]:
            # When b is pressed videoChange is 1
            style_name = "red"
            estado_animo_sistema = 4
            break
        if info == [['fear']]:
            # When b is pressed videoChange is 1
            style_name = "black"
            estado_animo_sistema = 5
            break
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        # cv.imshow('frame', gray)
        #if cv.waitKey(1) ==  ord('q'):
           # break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
    # elijo al azar una posición de columna
    ind1 = random.randint(1, 3)
    # abro la OPI correspondiente a esa columna y estado de ánimo
    OPI = asociacion [ind1][estado_animo_sistema-1]

    imagen_actual = eval ("funciones_auxiliares."+OPI+"(111)")
    #convirtiendo ambas imagenes a numpy arrays
    imagen_vieja = np.asarray(imagen_vieja)
    imagen_actual = np.asarray(imagen_actual)
    #cambio tamaño imagenes para cambiar tamaño ventana
    imagen_vieja = cv_i.resize(imagen_vieja, dsize=(height, width), interpolation=cv_i.INTER_CUBIC)
    imagen_actual = cv_i.resize(imagen_actual, dsize=(height, width), interpolation=cv_i.INTER_CUBIC)

    #haciendo la transición entre las dos imágenes (demora 0,1 seg = 1000 x 0.0001)
    for alpha in np.linspace(0, 1, 1000):
        beta = 1 - alpha
        pintura = cv_i.addWeighted(imagen_actual, alpha, imagen_vieja, beta, 0)
        cv_i.imshow('Pintura', pintura)
        time.sleep(0.0001)
        if cv_i.waitKey(1) == 27:
            break
    #con estos 29s de demora se cumplen los 40s de muestreo
    #time.sleep(29)
    print (datetime.datetime.now().time())
    if cv.waitKey(1) == ord('q'):
      break




