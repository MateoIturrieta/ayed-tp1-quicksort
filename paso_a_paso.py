# muestra el vector marcando entre [ ] los extremos del tramo
def mostrar(vector, inicio, fin, mensaje):
    texto = ""
    for i in range(len(vector)):
        if i == inicio or i == fin:
            texto = texto + "[" + str(vector[i]) + "] "
        else:
            texto = texto + str(vector[i]) + " "
    print(mensaje + ": " + texto)

def particionar(vector, bajo, alto):
    pivote = vector[alto]  # el pivote es el ultimo elemento
    print("Pivote elegido: " + str(pivote))
    i = bajo - 1
    for j in range(bajo, alto):
        if vector[j] <= pivote:
            i = i + 1
            temp = vector[i]
            vector[i] = vector[j]
            vector[j] = temp
            mostrar(vector, bajo, alto, "  Intercambio")
    # el pivote va a su posicion final
    temp = vector[i + 1]
    vector[i + 1] = vector[alto]
    vector[alto] = temp
    mostrar(vector, bajo, alto, "  Pivote ubicado")
    return i + 1

def quicksort(vector, bajo, alto):
    if bajo < alto:
        print("Ordenando desde indice " + str(bajo) + " hasta " + str(alto))
        posicion_pivote = particionar(vector, bajo, alto)
        # se ordenan las dos mitades
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
