from PIL import Image, ImageFilter
import funciones_auxiliares

imagen = funciones_auxiliares.trae_imagen()
imagen.show()
imagen = imagen.filter(ImageFilter.GaussianBlur(radius = 10))
imagen.show()