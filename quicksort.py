def mostrar(vector, inicio, fin, mensaje):
    # Función para visualizar el estado del vector en cada paso
    texto = ""
    for i in range(len(vector)):
        if i == inicio or i == fin:
            texto = texto + "[" + str(vector[i]) + "] "
        else:
            texto = texto + str(vector[i]) + " "
    print(mensaje + ": " + texto)

def particionar(vector, bajo, alto):
    pivote = vector[alto]  # elegimos el último elemento como pivote
    print("Pivote elegido: " + str(pivote))
    i = bajo - 1  # índice del menor elemento
    for j in range(bajo, alto):
        if vector[j] <= pivote:
            i = i + 1
            # Intercambio manual (swap) sin usar funciones externas
            temp = vector[i]
            vector[i] = vector[j]
            vector[j] = temp
            mostrar(vector, bajo, alto, "  Intercambio")
    # Colocamos el pivote en su posición final
    temp = vector[i + 1]
    vector[i + 1] = vector[alto]
    vector[alto] = temp
    mostrar(vector, bajo, alto, "  Pivote ubicado")
    return i + 1

def quicksort(vector, bajo, alto):
    if bajo < alto:
        print("Ordenando desde indice " + str(bajo) + " hasta " + str(alto))
        posicion_pivote = particionar(vector, bajo, alto)
        # Ordenamos recursivamente las dos mitades
        quicksort(vector, bajo, posicion_pivote - 1)
        quicksort(vector, posicion_pivote + 1, alto)

# ---------- PROGRAMA PRINCIPAL ----------
n = int(input("Ingrese la cantidad de elementos: "))
vector = [0] * n
for i in range(n):
    vector[i] = int(input("Elemento " + str(i) + ": "))

print("Vector original: " + str(vector))
print("")
quicksort(vector, 0, n - 1)
print("")
print("Vector ordenado: " + str(vector))
