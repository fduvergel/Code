from PIL import Image
import funciones_auxiliares

imagen1 = funciones_auxiliares.trae_imagen()
imagen1.show()

# sacando el tamaño de la imagen
ancho, alto = imagen1.size

# pixeles de seleccion del área
n = 100
m = 200

if n>ancho:
    n= ancho
if m>alto:
    m=alto

area = (0,0,n,m)
region = imagen1.crop(area)

region.show()

img_flip_H = region.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

img_flip_H.show()

imagen1.paste(img_flip_H, area)
imagen1.show()