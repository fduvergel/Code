import math
import random

import funciones_auxiliares

imagen1 = funciones_auxiliares.trae_imagen()
imagen2 = funciones_auxiliares.trae_imagen()

#hago iguales las dimensiones
imagen1, imagen2 = funciones_auxiliares.iguala_dim_imgs(imagen1, imagen2)
imagen1.show()
imagen2.show()

#escojo valor random de L entre 0 y 1
L = random.random()

#recorro imágenes
for i in range(0, imagen1.size[0]-1):
    for j in range(0, imagen1.size[1]-1):

        pixel_img1 = imagen1.getpixel((i,j))   # Extraigo el pixel (i,j) de la imagen1
        dist_pix_1 = (pixel_img1[0]**2 + pixel_img1[1]**2 + pixel_img1[2]**2) #calculo la "distancia al cuadrado" de ese pixel

        pixel_img2 = imagen2.getpixel((i,j))   # Extraigo el pixel (i,j) de la imagen1
        dist_pix_2= (pixel_img2[0]**2 + pixel_img2[1]**2 + pixel_img2[2]**2) #calculo la "distancia al cuadrado" de ese pixel

        #detectando "activación hebbiana", considero cada distancia de pixel como una celula,
        #si las dos celulas son aprox iguales se activan simultáneamente con la funcion definida que será la componente de color resultante
        if (int(dist_pix_1/10) == int(dist_pix_2/10)):
            #aqui voy a modificar las distancias con la formula
            D_pix = random.randint(0, int(dist_pix_1 / 10))
            Dist_heb = dist_pix_1 * L + D_pix
            #descompongo esta distancia al cuadrado, escojo una componente de color aleatoria, que será dependiente de la nueva dist  y del promedio por color de los otros dos colores de la primera imagen
            #escojo un color aleatorio
            ind_pix = random.randint(0,2)
            match ind_pix:
                case 0:
                    prom_verde = (pixel_img1[1] + pixel_img2[1])/2
                    prom_azul = (pixel_img1[2] + pixel_img2[2]) / 2
                    p_rojo_n = math.sqrt(abs(Dist_heb- prom_verde**2 - prom_azul**2))
                    # Modifico la imagen con el nuevo valor del pixel
                    imagen1.putpixel((i, j), (int(p_rojo_n), int(prom_verde), int(prom_azul)))
                case 1:
                    prom_rojo = (pixel_img1[0] + pixel_img2[0])/2
                    prom_azul = (pixel_img1[2] + pixel_img2[2])/2
                    p_verde_n = math.sqrt(abs(Dist_heb - prom_rojo**2 - prom_azul**2))
                    # Modifico la imagen con el nuevo valor del pixel
                    imagen1.putpixel((i, j), (int(prom_rojo), int(p_verde_n), int(prom_azul)))
                case 2:
                    prom_verde = (pixel_img1[1] + pixel_img2[1])/2
                    prom_rojo = (pixel_img1[0] + pixel_img2[0]) / 2
                    p_azul_n = math.sqrt(abs(Dist_heb - prom_verde**2 - prom_rojo**2))
                    # Modifico la imagen con el nuevo valor del pixel
                    imagen1.putpixel((i, j), (int(prom_rojo), int(prom_verde), int(p_azul_n)))
        else:
            #intercambio los valores de los pixeles aleatoriamente (así "modifico" un poco más la imagen)
            #tomara el valor del pixel de la derecha, si es el R, el valor de R será el de G, el de G será B y el de B será R
            imagen1.putpixel((i, j), (pixel_img1[1], pixel_img1[2], pixel_img1[0]))
# Muestro la imagen transformada
imagen1.show()