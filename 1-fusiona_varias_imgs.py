from PIL import Image
import funciones_auxiliares

# cantidad de imágenes a mezclar
ctdad_img = 4

imagen1 = funciones_auxiliares.trae_imagen()
imagen1.show()

# establezco ancho y altura mínimos"
ancho_min = imagen1.size[0]
altura_min = imagen1.size[1]

# escogiendo i-1 random imagenes"
for i in range(0, ctdad_img-1):
    imagen_i = funciones_auxiliares.trae_imagen()
    # mostrando la imagen
    imagen_i.show()
    # saco las dimensiones"
    ancho_i = imagen_i.size[0]
    altura_i = imagen_i.size[1]
    # busco la menor dimensión"
    if (ancho_i<ancho_min):
        ancho_min = ancho_i
    if (altura_i<altura_min):
        altura_min = altura_i
    # igualando los tamaños de las imágenes
    imagen1 = imagen1.resize((ancho_min, altura_min))
    imagen_i = imagen_i.resize((ancho_min, altura_min))
    # Haciendo el Blend
    img_blend = Image.blend(imagen1, imagen_i, 0.5)
    #guardo el blend en imagen1, para reutilizarlo en caso de ser necesario
    imagen1 = img_blend
    # mostrando el blend
    imagen1.show()

