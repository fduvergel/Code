import skimage.io as img
import math
import funciones_auxiliares

def logTransform(c, f):
    g = c * math.log(float(1 + f), 10);

    return g;


# Apply logarithmic transformation for an image

def logTransformImage(image, outputMax=255, inputMax=255):
    c = outputMax / math.log(inputMax + 1, 10)

    # Read pixels and apply logarithmic transformation

    for i in range(0, img.size[0] - 1):

        for j in range(0, img.size[1] - 1):
            # Get pixel value at (x,y) position of the image

            f = img.getpixel((i, j));

            # Do log transformation of the pixel

            redPixel = round(logTransform(c, f[0]));

            greenPixel = round(logTransform(c, f[1]));

            bluePixel = round(logTransform(c, f[2]));

            # Modify the image with the transformed pixel values

            img.putpixel((i, j), (redPixel, greenPixel, bluePixel));

    return image


# Display the image after applying the logarithmic transformation

img = funciones_auxiliares.trae_imagen()
#muestra la imagen
img.show()
logTransformedImage = logTransformImage(img);

logTransformedImage.show();
