"""Genera el grafico de resultados a partir del CSV del banco de pruebas."""

import csv
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AQUI = os.path.dirname(os.path.abspath(__file__))

AZUL, ROJO, GRIS = "#2563eb", "#c2410c", "#94a3b8"

archivo = open(os.path.join(AQUI, "resultados_quicksort.csv"), encoding="utf-8")
qs = list(csv.DictReader(archivo))
archivo.close()

prom = [r for r in qs if r["tipo"] == "aleatorio"]
peor = [r for r in qs if r["tipo"] == "ordenado"]

fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

# ---- (1) caso promedio: datos aleatorios ----
ax = axes[0]
n = [int(r["n"]) for r in prom]
t = [float(r["tiempo_s"]) for r in prom]
ax.plot(n, t, "o-", color=AZUL, lw=2, ms=6, label="Medido")
k = t[-1] / (n[-1] * math.log2(n[-1]))
ax.plot(n, [k * x * math.log2(x) for x in n], "--", color=GRIS, lw=1.8,
        label="Teórico O(n log n)")
ax.set_title("Datos aleatorios — caso promedio", fontweight="bold", fontsize=11)
ax.set_xlabel("Cantidad de elementos (n)", fontsize=9)
ax.set_ylabel("Tiempo (segundos)", fontsize=9)
ax.legend(fontsize=8.5)
ax.grid(alpha=.3)
ax.tick_params(labelsize=8)

# ---- (2) peor caso: vector ya ordenado ----
ax = axes[1]
np_ = [int(r["n"]) for r in peor]
tp = [float(r["tiempo_s"]) for r in peor]
ax.plot(np_, tp, "o-", color=ROJO, lw=2, ms=6, label="Medido")
k2 = tp[-1] / (np_[-1] ** 2)
ax.plot(np_, [k2 * x ** 2 for x in np_], "--", color=GRIS, lw=1.8,
        label="Teórico O(n²)")
ax.set_title("Vector ya ordenado — peor caso", fontweight="bold", fontsize=11)
ax.set_xlabel("Cantidad de elementos (n)", fontsize=9)
ax.set_ylabel("Tiempo (segundos)", fontsize=9)
ax.legend(fontsize=8.5)
ax.grid(alpha=.3)
ax.tick_params(labelsize=8)

plt.tight_layout()
salida = os.path.join(AQUI, "grafico_resultados.png")
plt.savefig(salida, dpi=170, facecolor="white")
print("Grafico guardado en:", salida)
