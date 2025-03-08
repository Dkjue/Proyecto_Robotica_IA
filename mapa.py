import numpy as np
import matplotlib.pyplot as plt

# Crear el mapa con fondo blanco
mapa = np.ones((2800, 2800))

# Nuevo Mapa 
# Paredes horizontales
mapa[400*6, 400:400]=0
mapa[400*6, 400*2:400*3]=0
mapa[400*5, 400:400*2]=0
mapa[400*5, 400*3:400*4]=0
mapa[400*4, 400*2:400*3]=0
mapa[400*4, 400*4:400*5]=0
mapa[400*3, 400*3:400*4]=0
mapa[400*3, 400*5:400*6]=0
mapa[400*2, 400*4:400*5]=0
mapa[400*1, 400*5:400*6]=0
mapa[400*2, 0:400]=0
mapa[400*1, 0:400]=0
mapa[400*1, 400*3:400*4]=0
mapa[400*2, 400*2:400*3]=0
mapa[400*6, 400*4:400*6]=0
mapa[400*5, 400*5:400*6]=0

# Paredes verticales
mapa[400:400*2, 400*5]=0
mapa[400:400*2, 400*5]=0
mapa[400*3:400*4, 400*5]=0
mapa[400*2:400*3, 400*6]=0
mapa[400*2:400*3, 400*4]=0
mapa[400*4:400*6, 400*4]=0
mapa[400*3:400*4, 400*3]=0
mapa[400*5:400*6, 400*3]=0
mapa[400*4:400*5, 400*2]=0
mapa[400*6:400*7, 400*2]=0
mapa[400*4:400*6, 400*1]=0
mapa[400*2:400*4, 400*1]=0
mapa[400*1:400*3, 400*2]=0
mapa[400*1:400*2, 400*3]=0
mapa[400*4:400*6, 400*6]=0

# Crear la visualización
plt.figure(figsize=(10, 10))
plt.imshow(mapa, cmap='gray', origin='upper')
plt.title('Mapa')
plt.xlabel('X')
plt.ylabel('Y')

# Añadir puntos en el centro de cada celda de una cuadrícula de 400x400
grid_size = 400
x_coords = np.arange(grid_size // 2, mapa.shape[1], grid_size)
y_coords = np.arange(grid_size // 2, mapa.shape[0], grid_size)
x_grid, y_grid = np.meshgrid(x_coords, y_coords)

# Plotear los puntos
plt.scatter(x_grid, y_grid, color='red', s=10)  # Puedes ajustar el tamaño del punto con 's'

plt.show()