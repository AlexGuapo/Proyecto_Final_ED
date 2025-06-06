# Selection Sort

Selection Sort es un algoritmo de ordenamiento que divide la lista en dos partes: una ordenada y otra no. En cada iteración, encuentra el valor mínimo de la parte no ordenada y lo coloca en la posición correspondiente de la parte ordenada.

##  ¿Cómo funciona?

1. Recorre la lista buscando el valor más pequeño.
2. Lo intercambia con el primer elemento no ordenado.
3. Repite el proceso con el resto de la lista.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n²)       |
| Promedio     | O(n²)       |
| Peor caso    | O(n²)       |

##  Ventajas

- Fácil de implementar
- Funciona bien con listas pequeñas
- Menor número de intercambios que otros algoritmos simples

##  Desventajas

- Siempre realiza O(n²) comparaciones
- No es estable (puede desordenar elementos iguales)

##  Ejemplo de entrada y salida

```python
Entrada: [64, 25, 12, 22, 11]
Salida:  [11, 12, 22, 25, 64]
