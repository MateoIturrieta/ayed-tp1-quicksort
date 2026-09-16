# Quicksort con pivote en el ultimo elemento - Grupo 38

import random
import time

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

        bajos = [0]
        altos = [len(v) - 1]

        while len(bajos) > 0:
            bajo = bajos.pop()
            alto = altos.pop()

            if bajo < alto:
                pivote = v[alto]    # el pivote es el ultimo
                i = bajo - 1

                for j in range(bajo, alto):
                    comparaciones = comparaciones + 1
                    if v[j] <= pivote:
                        i = i + 1
                        aux = v[i]
                        v[i] = v[j]
                        v[j] = aux

                # el pivote va a su posicion definitiva
                aux = v[i + 1]
                v[i + 1] = v[alto]
                v[alto] = aux
                p = i + 1

                # se anotan los tramos que faltan ordenar
                if p + 1 < alto:
                    bajos.append(p + 1)
                    altos.append(alto)
                if bajo < p - 1:
                    bajos.append(bajo)
                    altos.append(p - 1)

        fin = time.perf_counter()
        tiempo = round(fin - inicio, 5)

        print("  ", nombres[caso], ":", comparaciones, "comparaciones en", tiempo, "segundos")

    print()
