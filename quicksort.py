# Quicksort con el pivote en el ultimo elemento
# Trabajo Practico - Algoritmo y Estructura de Datos - Grupo 38
#
# Se ordenan vectores de distintos tamanios y se cuenta cuantas
# comparaciones hace el algoritmo en cada caso.

import random

random.seed(38)     # asi los numeros al azar son siempre los mismos

tamanios = [500, 1000, 2000, 4000, 8000]


for n in tamanios:

    # Vector desordenado: n numeros al azar
    desordenado = []
    for k in range(n):
        desordenado.append(random.randint(1, 100000))

    # Vector ya ordenado: 0, 1, 2, ..., n-1
    ordenado = []
    for k in range(n):
        ordenado.append(k)

    print("Vector de", n, "elementos")

    vectores = [desordenado, ordenado]
    nombres = ["desordenado", "ya ordenado"]

    for caso in range(len(vectores)):

        v = vectores[caso]
        comparaciones = 0

        # ---------------- QUICKSORT ----------------

        # Dos listas con los tramos que faltan ordenar.
        # Al principio hay uno solo: el vector completo.
        bajos = [0]
        altos = [len(v) - 1]

        while len(bajos) > 0:

            # Se saca el ultimo tramo anotado
            bajo = bajos.pop()
            alto = altos.pop()

            # Un tramo de 0 o 1 elemento ya esta ordenado
            if bajo < alto:

                pivote = v[alto]        # el pivote es SIEMPRE el ultimo
                i = bajo - 1            # hasta aca llegan los menores o iguales

                for j in range(bajo, alto):

                    comparaciones = comparaciones + 1

                    if v[j] <= pivote:

                        i = i + 1

                        # intercambio v[i] con v[j]
                        aux = v[i]
                        v[i] = v[j]
                        v[j] = aux

                # el pivote se pone en el medio de las dos zonas:
                # esa es su posicion definitiva
                aux = v[i + 1]
                v[i + 1] = v[alto]
                v[alto] = aux

                p = i + 1

                # Se anotan los dos tramos que quedan a los costados,
                # pero solo si tienen 2 o mas elementos
                if p + 1 < alto:
                    bajos.append(p + 1)
                    altos.append(alto)

                if bajo < p - 1:
                    bajos.append(bajo)
                    altos.append(p - 1)

        # --------------------------------------------

        print("  ", nombres[caso], ":", comparaciones, "comparaciones")

    print()
