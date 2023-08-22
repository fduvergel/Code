# aprendizaje hebbiano por componente RGB pixeles
import random

import funciones_auxiliares

imagen1 = funciones_auxiliares.trae_imagen()
imagen2 = funciones_auxiliares.trae_imagen()

p_rojo_n=0
p_verde_n=0
p_azul_n=0

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
        p_rojo_1 = pixel_img1[0] # Extraigo valor color rojo
        p_verde_1 = pixel_img1[1]  # Extraigo valor color verde
        p_azul_1 = pixel_img1[2]  # Extraigo valor color azul

        D_rojo = random.randint(0, int (p_rojo_1/10))
        D_verde = random.randint(0, int (p_verde_1 / 10))
        D_azul = random.randint(0, int (p_azul_1 / 10))

        pixel_img2 = imagen2.getpixel((i,j))   # Extraigo el pixel (i,j) de la imagen2
        p_rojo_2 = pixel_img2[0] # Extraigo valor color rojo
        p_verde_2 = pixel_img2[1]  # Extraigo valor color verde
        p_azul_2 = pixel_img2[2]  # Extraigo valor color azul

        #detectando "aprendizaje hebbiana", considero cada integrante del color del pixel como una celula, si las dos celulas son iguales se activan simultáneamente con la funcion definida que será la componente de color resultante
        if (p_rojo_1 == p_rojo_2):
            p_rojo_n = p_rojo_1*L + D_rojo
            # normalizo en caso de ser necesario
            if (p_rojo_n > 255):
                p_rojo_n = p_rojo_n / 255
        if (p_verde_1 == p_verde_2):
            p_verde_n = p_verde_1 * L + D_verde
            # normalizo en caso de ser necesario
            if (p_verde_n > 255):
                p_verde_n = p_verde_n / 255
        if (p_azul_1 == p_azul_2):
            p_azul_n = p_azul_1 * L + D_azul
            # normalizo en caso de ser necesario
            if (p_azul_n > 255):
                p_azul_n = p_azul_n / 255

       # Modifico la imagen con el nuevo valor del pixel
        imagen1.putpixel((i,j),(int (p_rojo_n), int (p_verde_n), int (p_azul_n)))

# Muestro la imagen transformada
imagen1.show()