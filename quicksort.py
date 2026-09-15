# Quicksort con el pivote en el ultimo elemento
# Trabajo Practico - Algoritmo y Estructura de Datos - Grupo 38


v = [38, 27, 43, 3, 9, 82, 10]

print("Vector original:", v)
print()


# Dos listas con los tramos que faltan ordenar.
# Al principio hay uno solo: desde la posicion 0 hasta la ultima.
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

        print("Pivote", pivote, "-> posicion", p, ":", v)

        # Se anotan los dos tramos que quedan a los costados,
        # pero solo si tienen 2 o mas elementos
        if p + 1 < alto:
            bajos.append(p + 1)
            altos.append(alto)

        if bajo < p - 1:
            bajos.append(bajo)
            altos.append(p - 1)


print()
print("Vector ordenado:", v)
