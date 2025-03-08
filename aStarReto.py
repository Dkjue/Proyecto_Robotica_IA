import heapq
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import time

# Creación de clase nodo
class Nodo:
    def __init__(self, posicion, padre=None):
        self.posicion = posicion
        self.padre = padre
        self.g = np.sqrt((posicion[0]-objetivo[0])**2 + (posicion[0]-objetivo[1])**2)  # Inicializar con infinito para los costos

    def __eq__(self, otro):
        return self.posicion == otro.posicion

    def __lt__(self, otro):
        return self.g < otro.g

def obtener_camino(nodo):
    camino = []
    actual = nodo
    while actual is not None:
        camino.append(actual.posicion)
        actual = actual.padre
    return camino[::-1]

def es_colision(mapa, x, y, tamano_robot):
    ancho, alto = tamano_robot
    
    if x <= 0 or x + ancho > mapa.shape[0] or y <= 0 or y + alto > mapa.shape[1]:
        return True
    for i in range(int(ancho/2)):
        for j in range(int(ancho/2)):
            if mapa[x + i, y + j] != 0 or mapa[x - i, y - j] != 0:
                return True
    return False

def aStar(mapa, inicio, objetivo, tamano_robot=(200, 200), paso=200):
    nodos_abiertos = []
    nodos_cerrados = set()
    nodos_explorados = []

    nodo_inicio = Nodo(inicio)
    nodo_inicio.g = 0  # El costo inicial es 0
    nodo_objetivo = Nodo(objetivo)

    heapq.heappush(nodos_abiertos, nodo_inicio)
    costos = {inicio: 0}
    padres = {inicio: None}

    while nodos_abiertos:
        nodo_actual = heapq.heappop(nodos_abiertos)
        nodos_cerrados.add(nodo_actual.posicion)

        if nodo_actual == nodo_objetivo:
            return obtener_camino(nodo_actual), nodos_explorados

        (x, y) = nodo_actual.posicion
        vecinos = [
            (x - paso, y),
            (x + paso, y),
            (x, y - paso),
            (x, y + paso)
        ]

        for siguiente in vecinos: #itera las posiciones vecinas
            (x, y) = siguiente
            if not es_colision(mapa, x, y, tamano_robot):
                nuevo_costo = nodo_actual.g + 1 #seria el costo del actual 

                if siguiente not in nodos_cerrados: #No puede volver a su posicion inicial
                    if siguiente not in costos or nuevo_costo < costos[siguiente]:
                        costos[siguiente] = nuevo_costo
                        padres[siguiente] = nodo_actual
                        heapq.heappush(nodos_abiertos, Nodo(siguiente, nodo_actual))
                        nodos_explorados.append(siguiente)


    return None, nodos_explorados
def reducirGrupos (valores):
    listaNueva = []
    i = 0
    while i < len(valores):
        suma = valores[i]
        j = i + 1
        while j < len(valores) and valores[j] == valores[i]:
            suma += valores[j]
            j += 1
        listaNueva.append(suma)
        i = j  # continuamos desde esta posición
    return listaNueva
# Definición del mapa con paredes de 3 mm y puntos de 20 cm
mapa = np.zeros((2800, 2800))

# Paredes horizontales
#apa[400*6, 0:400]=1
mapa[400*6, 400*2:400*3]=1
mapa[400*5, 400:400*2]=1
mapa[400*5, 400*3:400*4]=1
mapa[400*4, 400*2:400*3]=1
mapa[400*4, 400*4:400*5]=1
mapa[400*3, 400*3:400*4]=1
mapa[400*3, 400*5:400*6]=1
mapa[400*2, 400*4:400*5]=1
mapa[400*1, 400*5:400*6]=1
mapa[400*2, 0:400]=1
mapa[400*1, 0:400]=1
mapa[400*1, 400*3:400*4]=1
mapa[400*2, 400*2:400*3]=1
mapa[400*6, 400*4:400*6]=1
mapa[400*5, 400*5:400*6]=1

# Paredes verticales
mapa[400:400*2, 400*5]=1
mapa[400:400*2, 400*5]=1
mapa[400*3:400*4, 400*5]=1
mapa[400*2:400*3, 400*6]=1
mapa[400*2:400*3, 400*4]=1
mapa[400*4:400*6, 400*4]=1
mapa[400*3:400*4, 400*3]=1
mapa[400*5:400*6, 400*3]=1
mapa[400*4:400*5, 400*2]=1
mapa[400*6:400*7, 400*2]=1
mapa[400*5:400*6, 400*1]=1
mapa[400*2:400*4, 400*1]=1
mapa[400*1:400*3, 400*2]=1
mapa[400*1:400*2, 400*3]=1
mapa[400*4:400*6, 400*6]=1

mapa[400*4:400*5, 400*1]=1

# inicio = (2600, 400*3+200)
inicio = (200 * 7, 200*5)
objetivo = (200*5, 200)
tiempo1 = time.time()
camino, nodos_explorados = aStar(mapa, inicio, objetivo)
tiempo2 = time.time()
dif = tiempo2 - tiempo1 
print(f'El tiempo de ejecución es: {dif} segundos')
# Configuración para visualización
fig = plt.figure(figsize=(15, 10))  # Tamaño de la figura
gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1])  # Mapa a la izquierda, mapa con Dijkstra a la derecha

# Subgráfico para el mapa original
ax0 = plt.subplot(gs[0])
ax0.imshow(mapa, cmap='Greys', origin='upper')
ax0.set_title('Mapa Original')

# Subgráfico para el mapa con el camino de Dijkstra
ax1 = plt.subplot(gs[1])
ax1.imshow(mapa, cmap='Greys', origin='upper')

# Visualización del camino en el mapa con Dijkstra
if camino:
    camino_x, camino_y = zip(*camino)
    ax1.plot(camino_y, camino_x, 'bo-', markersize=10, label='Camino')

# Visualización de los nodos explorados
if nodos_explorados:
    exp_x, exp_y = zip(*nodos_explorados)
    ax1.plot(exp_y, exp_x, 'ro', markersize=5, label='Nodos Explorados')

# Impresión de los puntos del camino
instruction="{"
vx = []
vy = []
distance = 40.0/100 + 3 / 100
Velx = 1 * distance #valor de velocidad
Vely = 1 * distance #valor de velocidad
punto_prev = inicio
if camino:
    print("Puntos del camino:")
    for punto in camino:
        #print(f"({punto[1]}, {punto[0]})")
        #instruction+=(f"{{{(punto[0]-200)/1000}, {(punto[1]-200)/1000}, 0}}, ")
        #if punto == camino[-1]:
            #print(instruction)
        if punto == inicio:
            continue
        if punto[0] == punto_prev[0]:
            #Significa que avanzó en X, fue derecha (+) o izquierda (-) ?
            if punto[1] > punto_prev [1]: #significa que fue Vx(+)
                vx.append(Velx)
            else: #Significa que fue Vx (-)
                vx.append (-Velx)
            vy.append (0)
        else:
            #Significa que avanzó en Y
            if punto[0] > punto_prev [0]:
                vy.append (Vely)
            else: 
                vy.append (-Vely)
            vx.append(0)
        punto_prev = punto

def eliminar_posiciones_pares(lista):
    return [x for i, x in enumerate(lista) if i % 2 != 0]

vy = eliminar_posiciones_pares(vy)
vx = eliminar_posiciones_pares(vx)
# Agrupamos los valores repetidos
vyReducido = reducirGrupos (vy)
vxReducido = reducirGrupos (vx)
def aproximar_lista(lista):
    return [round(x, 2) for x in lista]

vx = aproximar_lista(vxReducido)
vy = aproximar_lista(vyReducido) 
# Para validar
# for i in range(len(vx)):
#     print(f"{{{vx[i]}, {vy[i]}, 0}}")

# Hacemos el arreglo
for velY in vy:
    instruction += (f"{velY}, ")
instruction = instruction[: -2]
instruction += "},\n{"
for velX in vx:
    instruction += (f"{velX}, ")
instruction = instruction[: -2]
instruction += "},\n{"
for theta in vx:
    instruction += "0, "
instruction = instruction[: -2]
instruction += "}"

print(instruction)

# Marcamos el inicio y el objetivo
ax1.plot(inicio[1], inicio[0], 'gs', markersize=10, label='Inicio')
ax1.plot(objetivo[1], objetivo[0], 'ms', markersize=10, label='Objetivo')

# Leyenda y etiquetas
ax1.legend()
ax1.set_xlabel('X')
ax1.set_ylabel('Y')


plt.tight_layout()
plt.show()
