import numpy as np

minha_lista_1=np.array([[1, 2, 3],[3, 4, 5],[2, 5, 6]])

# calcula a inversa da matriz quadrada
x = np.linalg.inv(minha_lista_1)

print(x)