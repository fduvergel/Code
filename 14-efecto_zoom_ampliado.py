import cv2
import numpy as np
import time


imgpath1 = "bosque.jpg"
imgpath2 = "cielo.jpg"

img1 = cv2.imread(imgpath1, 1)
img2 = cv2.imread(imgpath2, 1)

img1 = cv2.resize(img1, dsize=(640,640), interpolation=cv2.INTER_CUBIC)
img2 = cv2.resize(img2, dsize=(640,640), interpolation=cv2.INTER_CUBIC)

for i in np.linspace(0, 1, 1000):
    alpha = i
    beta = 1 - alpha
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)
    cv2.imshow('Transition', output)
    time.sleep(0.0001)
    if cv2.waitKey(1) == 27:
        break
