# Radix Sort

Radix Sort es un algoritmo de ordenamiento no comparativo que ordena los números procesando sus dígitos, uno a uno. Ordena de forma estable usando un método auxiliar como Counting Sort para cada posición decimal.

##  ¿Cómo funciona?

1. Encuentra la cantidad máxima de dígitos entre los números.
2. Ordena todos los números por el dígito menos significativo (unidad), luego por decenas, centenas, etc.
3. Usa listas auxiliares (buckets) para agrupar por cada dígito.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(nk)       |
| Promedio     | O(nk)       |
| Peor caso    | O(nk)       |

Donde `n` es el número de elementos y `k` la cantidad de dígitos.

##  Ventajas

- Muy eficiente para enteros con longitud de dígitos acotada
- No realiza comparaciones
- Estable

##  Desventajas

- Solo funciona con números enteros no negativos
- Uso extra de memoria por los buckets

##  Ejemplo de entrada y salida

```python
Entrada: [170, 45, 75, 90, 802, 24, 2, 66]
Salida:  [2, 24, 45, 66, 75, 90, 170, 802]
