import random
import sys
import time

# con un vector ya ordenado la recursion llega a n niveles
sys.setrecursionlimit(10000)

comparaciones = 0

def particionar(vector, bajo, alto):
    global comparaciones
    pivote = vector[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        comparaciones = comparaciones + 1
        if vector[j] <= pivote:
            i = i + 1
            temp = vector[i]
            vector[i] = vector[j]
            vector[j] = temp
    temp = vector[i + 1]
    vector[i + 1] = vector[alto]
    vector[alto] = temp
    return i + 1

def quicksort(vector, bajo, alto):
    if bajo < alto:
        posicion_pivote = particionar(vector, bajo, alto)
        quicksort(vector, bajo, posicion_pivote - 1)
        quicksort(vector, posicion_pivote + 1, alto)

# ---------- PRUEBAS ----------
random.seed(38)
tamanios = [500, 1000, 2000, 4000, 8000]

for n in tamanios:
    desordenado = []
    for k in range(n):
        desordenado.append(random.randint(1, 100000))

    ordenado = []
    for k in range(n):
        ordenado.append(k)

    print("Vector de", n, "elementos")
    vectores = [desordenado, ordenado]
    nombres = ["desordenado", "ya ordenado"]

    for caso in range(len(vectores)):
        v = vectores[caso]
        comparaciones = 0
        inicio = time.perf_counter()
        quicksort(v, 0, len(v) - 1)
        fin = time.perf_counter()
        tiempo = round(fin - inicio, 5)
        print("  ", nombres[caso], ":", comparaciones, "comparaciones en", tiempo, "segundos")
    print()
