import random
from PIL import Image
import math
import funciones_auxiliares



#transformacion coseno de una imagen

imagen1 = funciones_auxiliares.trae_imagen()
imagen1.show()

for i in range(0, imagen1.size[0]-1):

    for j in range(0, imagen1.size[1]-1):

        pixel = imagen1.getpixel((i,j))   # Extraigo el pixel
        p_rojo = pixel[0] # Extraigo valor color rojo
        p_verde = pixel[1]  # Extraigo valor color verde
        p_azul = pixel[2]  # Extraigo valor color azul

        # aplico funcion seno a todos los colores (la función sin usa como argumento el radian y es flotante)
        #convierto a flotante los enteros para pasarlo a la funcion seno
        rojo = float (p_rojo)
        verde = float (p_verde)
        azul = float (p_azul)
        #aplico funcion coseno
        rojo = math.cos(rojo)
        verde = math.cos (verde)
        azul = math.cos (azul)
        #normalizo a 255 y lo hago positivo
        rojo = abs(rojo)*255
        verde = abs(verde)*255
        azul = abs(azul)*255
        #convierto a entero
        rojo = int(rojo)
        verde = int(verde)
        azul = int(azul)

        # Modifico la imagen con el nuevo valor del pixel
        imagen1.putpixel((i,j),(rojo, verde, azul))

# Muestro la imagen transformada
imagen1.show()