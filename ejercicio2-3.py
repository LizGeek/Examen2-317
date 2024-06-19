import cv2
import numpy as np

# Leer las imágenes
img1 = cv2.imread('imagen1.jpeg')
img2 = cv2.imread('imagen2.jpeg')

# Redimensionar la segunda imagen para que tenga el mismo tamaño que la primera
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Suma de imágenes
suma = cv2.add(img1, img2)
# O usando el operador +
# suma = img1 + img2

# Resta de imágenes
resta = cv2.subtract(img1, img2)
# O usando el operador -
# resta = img1 - img2

# Mostrar las imágenes
cv2.imshow('Imagen 1', img1)
cv2.imshow('Imagen 2', img2)
cv2.imshow('Suma', suma)
cv2.imshow('Resta', resta)

# Esperar a que se pulse una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
