def particionar(vector, bajo, alto):
    pivote = vector[alto]  # el pivote es el ultimo elemento
    i = bajo - 1
    for j in range(bajo, alto):
        if vector[j] <= pivote:
            i = i + 1
            temp = vector[i]
            vector[i] = vector[j]
            vector[j] = temp
    # el pivote va a su posicion final
    temp = vector[i + 1]
    vector[i + 1] = vector[alto]
    vector[alto] = temp
    return i + 1

def quicksort(vector, bajo, alto):
    if bajo < alto:
        posicion_pivote = particionar(vector, bajo, alto)
        # se ordenan las dos mitades
        quicksort(vector, bajo, posicion_pivote - 1)
        quicksort(vector, posicion_pivote + 1, alto)
