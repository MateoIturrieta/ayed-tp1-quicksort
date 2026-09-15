# Quicksort — Trabajo Práctico N.º 1

**Algoritmo y Estructura de Datos** · Ingeniería en Sistemas de Información · Comisión 2 · UTN · 2026

Método asignado: **ordenación rápida (Quicksort)** con el **pivote fijo en el último elemento** del
tramo, conocida como *partición de Lomuto*. Referencia: Joyanes Aguilar, *Fundamentos de
Programación*, capítulo 6.

> El código está escrito de forma **lineal, sin definir funciones**. Como no hay funciones tampoco
> hay recursión, así que la repetición sobre cada mitad se resuelve con una **pila explícita**: una
> lista donde se anotan los tramos que faltan ordenar. Es lo mismo que hace la recursión por dentro,
> sólo que acá la pila está a la vista y se puede contar.

## Archivos

| Archivo | Qué hace |
|---|---|
| `quicksort.py` | Implementación del método. Ordena un vector de ejemplo, imprime el vector después de cada partición, cuenta comparaciones e intercambios y verifica el resultado contra `sorted()`. |
| `banco_de_pruebas.py` | Mide los tiempos de ejecución reales y genera `resultados_quicksort.csv`. |
| `graficos.py` | Genera `grafico_resultados.png` a partir del CSV. |
| `resultados_quicksort.csv` | Resultados crudos de las mediciones. |
| `visualizador.html` | Visualización interactiva del algoritmo paso a paso. Se abre con doble clic en cualquier navegador. |

## Cómo ejecutarlo

Requiere Python 3. Para el gráfico hace falta además `matplotlib`.

```bash
python quicksort.py           # ordena el vector de ejemplo y muestra cada partición
python banco_de_pruebas.py    # mide los tiempos (tarda ~1 minuto)
python graficos.py            # genera el gráfico a partir del CSV
```

## Resultados medidos

Python 3.12.0 sobre Windows 11. Medición con `time.perf_counter()`, 3 repeticiones por medición
tomando el mejor tiempo, semilla fija `random.seed(2026)` para que las pruebas sean reproducibles.

**Datos aleatorios — caso promedio, O(n log n)**

| n | Tiempo | × tiempo al duplicar n | Comparaciones |
|---:|---:|---:|---:|
| 10.000 | 0,027 s | — | 157.213 |
| 50.000 | 0,170 s | — | 934.560 |
| 100.000 | 0,352 s | ×2,1 | 1.944.625 |
| 200.000 | 0,799 s | ×2,3 | 4.306.806 |

**Vector ya ordenado — peor caso, O(n²)**

| n | Tiempo | × tiempo al duplicar n | Comparaciones |
|---:|---:|---:|---:|
| 1.000 | 0,061 s | — | 499.500 |
| 2.000 | 0,249 s | ×4,1 | 1.999.000 |
| 4.000 | 1,101 s | ×4,4 | 7.998.000 |
| 8.000 | 4,259 s | ×3,9 | 31.996.000 |

Con datos aleatorios, duplicar `n` multiplica el tiempo por poco más de 2. Con el vector ya ordenado
lo multiplica por 4, que es 2²: el método degenera a O(n²) porque el pivote fijo al final resulta ser
siempre el mayor del tramo.

Las 31.996.000 comparaciones medidas con n = 8.000 coinciden **exactamente** con la fórmula teórica
del peor caso, n·(n−1)/2.
