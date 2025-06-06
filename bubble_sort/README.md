# Bubble Sort

Bubble Sort es un algoritmo de ordenamiento simple que recorre repetidamente la lista, comparando elementos adyacentes y realizando intercambios si están en el orden incorrecto. Es uno de los algoritmos más fáciles de entender, pero también uno de los menos eficientes para listas grandes.

##  ¿Cómo funciona?

1. Compara el primer par de elementos.
2. Si están en orden incorrecto, los intercambia.
3. Repite el proceso hasta que la lista esté ordenada.

Este proceso se repite tantas veces como elementos haya en la lista.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n)        |
| Promedio     | O(n²)       |
| Peor caso    | O(n²)       |

##  Ventajas

- Implementación muy sencilla
- Útil para listas pequeñas o casi ordenadas

##  Desventajas

- Muy ineficiente para listas grandes
- Requiere muchas comparaciones

##  Ejemplo de entrada y salida

```python
Entrada: [64, 34, 25, 12, 22, 11, 90]
Salida:  [11, 12, 22, 25, 34, 64, 90]
