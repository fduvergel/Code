from PIL import Image, ImageFilter
import random
import funciones_auxiliares

imagen1 = funciones_auxiliares.trae_imagen()
imagen1.show()
# sacando el tamaño de la imagen
ancho, alto = imagen1.size
#voy a seleccionar 10 areas
for i in range(1, 10):
    # pixeles de seleccion del área
    n = random.randint(0, 255)
    m = random.randint(0, 255)
    d = random.randint(0, 120)
    fin_n = n+d
    fin_m = m+d
    if fin_n>ancho:
        fin_n= ancho
    if fin_m>alto:
        fin_m=alto
    area = (n,m,fin_n,fin_m)
    region = imagen1.crop(area)
    gaus_reg = region.filter(ImageFilter.GaussianBlur(radius = 5))
    imagen1.paste(gaus_reg, area)
imagen1.show()