import funciones_auxiliares

imagen1 = funciones_auxiliares.trae_imagen()
imagen1.show()

for i in range(0, imagen1.size[0]-1):

    for j in range(0, imagen1.size[1]-1):

        pixel = imagen1.getpixel((i,j))   # Extraigo el pixel
        rojo = pixel[0] # Extraigo valor color rojo
        verde = pixel[1]  # Extraigo valor color verde
        azul = pixel[2]  # Extraigo valor color azul

        #Si el pixel rojo es menor de 150, lo apago
        if (rojo<=150):
            rojo = 0
        # Modifico la imagen con el nuevo valor del pixel
        imagen1.putpixel((i,j),(rojo, verde, azul))

# Muestro la imagen transformada
imagen1.show()
