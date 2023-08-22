import librosa
import funciones_auxiliares
# Paquetes necesarios para la exploración de datos
import matplotlib.pyplot as plt
import numpy as np

audio = 'la-vida-es-un-carnaval-ringtones-.mp3'

# decodifica el archivo de audio en un arreglo unidimensional y, sample_rates guarda la frecuencia de muestreo
y, sampling_rate = librosa.load(audio)

T = y.size / sampling_rate  # tiempo total audio
dt = 1 / sampling_rate   # diferencial de tiempo
t = np.r_[0:T:dt]   # arreglo numpy que de 0 a T en intervalos dt

X = librosa.stft(y)
X_dB = librosa.amplitude_to_db(np.abs(X))

dim_DB = X_dB.size

print(
    f'y[t] tiene {y.size} muestras',
    f'la frecuencia de muestreo es {sampling_rate * 1e-3}kHz',
    f'y(t) tiene {T:.1f}s '
    , sep='\n')

plt.figure(1)
plt.plot(t, y)
plt.xlabel('tiempo [s]')
plt.ylabel('amplitud[/]')
plt.title(r'$y(t)$', size=20)
plt.show()


im = funciones_auxiliares.trae_imagen()
im_modif = im.copy () #imagen que se modificará

#calculando cantidad total de pixeles 
ctdad_pixeles = im.size[0]*im.size[1]

if (dim_DB > ctdad_pixeles):

    rel_muestras_pixeles = dim_DB/ctdad_pixeles
    rel_muestras_pixeles = int(rel_muestras_pixeles)

    print(rel_muestras_pixeles)
    #como hay más muestras que pixeles, a cada pixel le corresponde un rango de muestras. De ese pixel, el color rojo será la primera muestra de ese rango, el color verde sera la muestra del medio y el color azul la última muestra de ese rango

    for i in range(0, im.size[0] - 1):
        for j in range(0, im.size[1] - 1):
            # asigno valores de pixeles
            rojo = X_dB[i,j]
            verde = X_dB[i,j]+1
            azul = X_dB[i,j]-1

            rojo = int(rojo)
            verde = int(verde)
            azul = int(azul)

            pix = im.getpixel((i,j))

            rojo = rojo + pix[0]
            verde = verde + pix[1]
            azul = azul + pix[2]

            im_modif.putpixel((i, j), (rojo, verde, azul))

im.show()
im_modif.show()
