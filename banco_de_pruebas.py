"""
Banco de pruebas: mide los tiempos de ejecucion reales de Quicksort.

VERSION SIN FUNCIONES: el algoritmo esta escrito de forma lineal dentro de los
ciclos de medicion. Es el mismo codigo de quicksort.py, sin los print del
paso a paso.

Genera:
  - resultados_quicksort.csv
  - Tablas impresas por consola

Las mediciones se hacen con time.perf_counter(), que es el reloj de mayor
precision que ofrece Python para medir intervalos.
"""

import csv
import os
import random
import sys
import time

SEMILLA = 2026          # semilla fija: las pruebas son reproducibles
REPETICIONES = 3        # cada medicion se repite y se toma el mejor tiempo

AQUI = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("BANCO DE PRUEBAS - TP AyED 2026")
print(f"Python {sys.version.split()[0]} | semilla = {SEMILLA} | "
      f"{REPETICIONES} repeticiones por medicion (se toma el mejor tiempo)")
print("=" * 78)


# ==========================================================================
# PRUEBA 1 y 2: QUICKSORT
#
# Se prueban dos formas de datos con el MISMO algoritmo:
#   - aleatorio : caso promedio
#   - ordenado  : peor caso del pivote fijo al final
# ==========================================================================
grupos = [
    ("aleatorio", [1000, 5000, 10000, 50000, 100000, 200000],
     "1) QUICKSORT - DATOS ALEATORIOS (caso promedio, O(n log n))", None),
    ("ordenado", [500, 1000, 2000, 4000, 8000],
     "2) QUICKSORT - DATOS YA ORDENADOS (PEOR CASO, O(n^2))",
     "   Con pivote fijo al final, si el vector ya viene ordenado la particion\n"
     "   deja un lado vacio y el otro con n-1 elementos: degenera a O(n^2)."),
]

filas_qs = []

for tipo, tamanos, titulo, aclaracion in grupos:

    print(f"\n\n{titulo}")
    print("-" * 78)
    if aclaracion:
        print(aclaracion)
        print("-" * 78)
    print(f"{'n':>9} | {'tiempo (s)':>11} | {'comparaciones':>14} | "
          f"{'intercambios':>13} | {'pila':>6}")
    print("-" * 78)

    for n in tamanos:

        # ---- generacion de los datos de prueba ----
        random.seed(SEMILLA)
        if tipo == "aleatorio":
            base = [random.randint(0, 1000000) for _ in range(n)]
        else:
            base = list(range(n))

        esperado = sorted(base)
        mejor_tiempo = float("inf")

        for repeticion in range(REPETICIONES):

            v = list(base)
            comparaciones = 0
            intercambios = 0
            pila_maxima = 0

            inicio = time.perf_counter()

            # ---------------- QUICKSORT (mismo codigo que quicksort.py) -------
            pila = [(0, len(v) - 1)]

            while pila:

                if len(pila) > pila_maxima:
                    pila_maxima = len(pila)

                bajo, alto = pila.pop()

                if bajo < alto:

                    pivote = v[alto]        # el pivote es SIEMPRE el ultimo
                    i = bajo - 1            # frontera de los "menores o iguales"

                    for j in range(bajo, alto):
                        comparaciones += 1
                        if v[j] <= pivote:
                            i += 1
                            if i != j:
                                v[i], v[j] = v[j], v[i]
                                intercambios += 1

                    v[i + 1], v[alto] = v[alto], v[i + 1]
                    intercambios += 1
                    p = i + 1

                    # Solo se apila un tramo si tiene 2 o mas elementos
                    if p + 1 < alto:
                        pila.append((p + 1, alto))     # mitad derecha
                    if bajo < p - 1:
                        pila.append((bajo, p - 1))     # mitad izquierda
            # ------------------------------------------------------------------

            fin = time.perf_counter()

            if fin - inicio < mejor_tiempo:
                mejor_tiempo = fin - inicio

            if v != esperado:
                print("ERROR: el vector no quedo ordenado")
                sys.exit(1)

        filas_qs.append({
            "n": n,
            "tipo": tipo,
            "tiempo_s": mejor_tiempo,
            "comparaciones": comparaciones,
            "intercambios": intercambios,
            "pila_maxima": pila_maxima,
        })

        print(f"{n:>9,} | {mejor_tiempo:>11.6f} | {comparaciones:>14,} | "
              f"{intercambios:>13,} | {pila_maxima:>6,}")


# ==========================================================================
# GUARDADO DE RESULTADOS
# ==========================================================================
archivo = open(os.path.join(AQUI, "resultados_quicksort.csv"), "w",
               newline="", encoding="utf-8")
escritor = csv.DictWriter(archivo, fieldnames=list(filas_qs[0].keys()))
escritor.writeheader()
escritor.writerows(filas_qs)
archivo.close()


print("\n" + "=" * 78)
print("Resultados guardados en resultados_quicksort.csv")
print("=" * 78)
