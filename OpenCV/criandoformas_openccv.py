# -*- coding: utf-8 -*-
"""CriandoFormas_OpencCV

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1itlEYZnJw8b42fuwkahvyEMBdc0LQjy1
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem_branco = np.zeros(shape=(512,512,3), dtype=np.int16)

imagem_branco.shape

plt.imshow(imagem_branco)

cv2.rectangle(imagem_branco, pt1=(384,10), pt2=(500,150),
              color=(0,0,255), thickness=10)

plt.imshow(imagem_branco)

cv2.rectangle(imagem_branco, pt1=(200,200), pt2=(300,300),
              color=(255,0,0), thickness=10)

plt.imshow(imagem_branco)

cv2.circle(img=imagem_branco, center=(100, 100), radius=50,
           color=(0,255,0), thickness=8)
plt.imshow(imagem_branco)

cv2.circle(img=imagem_branco, center=(400, 400), radius=50,
           color=(0,255,0), thickness=-1)
plt.imshow(imagem_branco)

cv2.line(imagem_branco, pt1=(0,0), pt2=(512, 512), 
         color=(102,255,255), thickness=5)
plt.imshow(imagem_branco)

"""##Texto"""

fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem_branco, text="Testando", org=(10,500),
            fontFace=fonte, fontScale=3, color=(255,255,255),
            thickness=3, lineType=cv2.LINE_AA)
plt.imshow(imagem_branco)

nova_imagem_branco = np.zeros(shape=(512, 512, 3), dtype=np.int32)

plt.imshow(nova_imagem_branco)

vertices = np.array([[100,300], [200,200], [400,300],
                    [200,400]], dtype=np.int32)

vertices

vertices.shape

points = vertices.reshape(-1,1,2)

vertices.shape

points.shape

points

cv2.polylines(nova_imagem_branco, [points], isClosed=True,
              color=(0,0,255), thickness=5)
plt.imshow(nova_imagem_branco)