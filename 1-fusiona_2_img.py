from PIL import Image
import funciones_auxiliares

# abro las dos imagenes    
imagen1 = funciones_auxiliares.trae_imagen()
imagen2 = funciones_auxiliares.trae_imagen()

#llamo a funcion para igualar dimensiones imagenes
imagen1, imagen2 = funciones_auxiliares.iguala_dim_imgs(imagen1, imagen2)

# Make sure the images have alpha channels
#image3.putalpha(1)
#image4.putalpha(1)

# Display the images
imagen1.show()
imagen2.show()

# Do an alpha composite of image4 over image3
Blend = Image.blend(imagen1, imagen2, 0.5)
#alphaBlended = Image.blend(image4, image3,.1)
#alphaBlended.show()

# Display the alpha composited image
Blend.show()
