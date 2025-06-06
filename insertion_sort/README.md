# Insertion Sort

Insertion Sort es un algoritmo de ordenamiento que construye la lista ordenada uno a uno, insertando cada nuevo elemento en su posición correcta respecto a los anteriores. Es eficiente para listas pequeñas o casi ordenadas.

##  ¿Cómo funciona?

1. Toma un elemento a partir del segundo.
2. Lo compara con los elementos anteriores.
3. Lo inserta en la posición correcta desplazando los mayores.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n)        |
| Promedio     | O(n²)       |
| Peor caso    | O(n²)       |

##  Ventajas

- Fácil de implementar
- Eficiente con listas pequeñas o casi ordenadas
- Estable (mantiene el orden de elementos iguales)

##  Desventajas

- Ineficiente con listas grandes
- Muchas comparaciones en el peor caso

##  Ejemplo de entrada y salida

```python
Entrada: [29, 10, 14, 37, 13]
Salida:  [10, 13, 14, 29, 37]
