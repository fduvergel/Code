from PIL import Image, ImageOps
import funciones_auxiliares

rango_pix = 300
nueva_img = Image.new("RGBA",(600,600))
for i in range(0, 600, rango_pix):
    for j in range(0, 600, rango_pix):
        imagen = funciones_auxiliares.trae_imagen()
        img_mod = ImageOps.fit(imagen,(rango_pix, rango_pix))
        nueva_img.paste(img_mod,(i,j))
        nueva_img.show()
