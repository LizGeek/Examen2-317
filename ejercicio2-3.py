import cv2
import numpy as np

# Cargar las imágenes
img1 = cv2.imread('imagen1.jpeg')
img2 = cv2.imread('imagen2.jpeg')

# Verificar si las imágenes se han cargado correctamente
if img1 is None:
    raise ValueError("La imagen 'imagen1.jpeg' no se pudo cargar. Verifica el archivo y la ruta.")
if img2 is None:
    raise ValueError("La imagen 'imagen2.jpeg' no se pudo cargar. Verifica el archivo y la ruta.")

# Asegurarse de que las imágenes sean del mismo tamaño
if img1.shape != img2.shape:
    raise ValueError("Las imágenes deben ser del mismo tamaño y tener el mismo número de canales")

# Suma de imágenes
suma = cv2.add(img1, img2)

# Resta de imágenes
resta = cv2.subtract(img1, img2)

# Guardar las imágenes resultantes
cv2.imwrite('suma.jpeg', suma)
cv2.imwrite('resta.jpeg', resta)

# Mostrar las imágenes resultantes
cv2.imshow('Suma', suma)
cv2.imshow('Resta', resta)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Operaciones completadas y guardadas como suma.jpeg y resta.jpeg")
