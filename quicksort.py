"""
Quicksort con pivote fijo en el ultimo elemento (particion de Lomuto).

Referencia: Joyanes Aguilar, "Fundamentos de Programacion", Cap. 6 - Ordenacion rapida.

VERSION SIN FUNCIONES: todo el algoritmo esta escrito de forma lineal.

Como no se usan funciones, tampoco se puede usar recursion (un algoritmo no
puede llamarse a si mismo si no es una funcion). En su lugar se lleva una PILA
con los tramos que todavia quedan pendientes de ordenar.

Eso no es un truco: es exactamente lo que hace la recursion por dentro. La
diferencia es que aca la pila esta a la vista y se puede imprimir.

La idea del metodo es DIVIDE Y VENCERAS:
  1. Se elige un pivote (aca: siempre el ultimo elemento del tramo).
  2. Se reacomoda el tramo de forma que queden a la izquierda los menores o
     iguales al pivote y a la derecha los mayores. El pivote queda en su
     posicion definitiva.
  3. Los dos tramos que quedan a los costados se guardan en la pila para
     resolverlos despues.
  4. Termina cuando la pila se vacia. Un tramo de 0 o 1 elemento no se apila:
     ya esta ordenado por definicion.
"""

# --------------------------------------------------------------------------
# DATOS DE ENTRADA
# --------------------------------------------------------------------------
v = [38, 27, 43, 3, 9, 82, 10]

original = list(v)          # se guarda una copia para verificar al final
mostrar_pasos = True        # poner en False para ver solo el resultado

print("Vector original :", v)
print()

# --------------------------------------------------------------------------
# CONTADORES
#
# Las comparaciones y los intercambios son la unidad de trabajo del metodo.
# Contarlos permite medir el esfuerzo del algoritmo sin que dependa de la
# velocidad de la maquina.
# --------------------------------------------------------------------------
comparaciones = 0
intercambios = 0
pila_maxima = 0             # cuantos tramos llego a haber pendientes a la vez

# --------------------------------------------------------------------------
# ALGORITMO
#
# La pila guarda los tramos (bajo, alto) que todavia hay que ordenar.
# Al principio hay uno solo: el vector completo.
# --------------------------------------------------------------------------
pila = [(0, len(v) - 1)]

while pila:

    if len(pila) > pila_maxima:
        pila_maxima = len(pila)

    bajo, alto = pila.pop()        # se saca el ultimo tramo que entro

    # CONDICION DE CORTE: un tramo de 0 o 1 elemento ya esta ordenado.
    # Si no se cumple bajo < alto, no se hace nada y se sigue con el siguiente.
    if bajo < alto:

        # ---------- PARTICION DE LOMUTO sobre el tramo v[bajo..alto] ----------
        pivote = v[alto]           # PASO 1: el pivote es SIEMPRE el ultimo
        i = bajo - 1               # PASO 2: frontera de la zona "menores o iguales"

        for j in range(bajo, alto):        # PASO 3: recorre el tramo
            comparaciones += 1
            if v[j] <= pivote:             # PASO 4: decide para cada elemento
                i += 1
                if i != j:
                    v[i], v[j] = v[j], v[i]    # lo manda a la zona izquierda
                    intercambios += 1
            # Si v[j] > pivote no se hace nada: queda del lado de los mayores.

        # PASO 5: el pivote se ubica justo despues de la zona de los menores.
        # Esa es su posicion DEFINITIVA: no se lo vuelve a tocar.
        v[i + 1], v[alto] = v[alto], v[i + 1]
        intercambios += 1
        p = i + 1

        if mostrar_pasos:
            print(f"  tramo [{bajo}..{alto}]  pivote={pivote:>3}  ->  {v}"
                  f"   (el {pivote} queda fijo en la posicion {p})")

        # PASO 6: quedan dos tramos por ordenar. Se apilan para mas tarde.
        #
        # Se apila primero la mitad DERECHA y despues la IZQUIERDA, porque la
        # pila devuelve siempre el ultimo que entro. De esta forma la mitad
        # izquierda se resuelve antes, igual que en la version recursiva.
        #
        # Solo se apila un tramo si tiene 2 o mas elementos. Apilar tramos de
        # 0 o 1 elemento seria trabajo al pedo: ya estan ordenados. Ademas,
        # evitarlo mantiene la pila chica en el peor caso.
        if p + 1 < alto:
            pila.append((p + 1, alto))     # mitad derecha
        if bajo < p - 1:
            pila.append((bajo, p - 1))     # mitad izquierda

# --------------------------------------------------------------------------
# RESULTADO
# --------------------------------------------------------------------------
print()
print("Vector ordenado :", v)
print()
print(f"Comparaciones   : {comparaciones}")
print(f"Intercambios    : {intercambios}")
print(f"Pila maxima     : {pila_maxima} tramos pendientes a la vez")

# Verificacion: el resultado debe coincidir con el sorted() de Python
if v == sorted(original):
    print()
    print("Verificado contra sorted() de Python: OK")
else:
    print()
    print("ERROR: el vector no quedo bien ordenado")
