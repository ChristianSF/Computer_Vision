# -*- coding: utf-8 -*-
"""Histogramas_OpenCV

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RNpVkSrVTOuXqHeg9k8D5-YwI3CH30Rh
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("/content/Tony-Stark.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

color = ( 'b' , 'g' , 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])
plt.show ()