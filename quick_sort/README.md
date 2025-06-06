# Quick Sort

Quick Sort es un algoritmo de ordenamiento que utiliza la estrategia de divide y vencerás. Selecciona un elemento como pivote y reorganiza la lista de modo que los elementos menores queden a su izquierda y los mayores a su derecha, aplicando el proceso recursivamente.

##  ¿Cómo funciona?

1. Elige un pivote (en este caso, el primer elemento).
2. Separa la lista en dos sublistas: menores y mayores al pivote.
3. Aplica Quick Sort a cada sublista.
4. Une los resultados con el pivote en medio.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n log n)  |
| Promedio     | O(n log n)  |
| Peor caso    | O(n²)       |

##  Ventajas

- Muy rápido en la práctica
- Bajo uso de memoria (versión in-place)
- Muy usado en librerías estándar

##  Desventajas

- Peor caso es O(n²) (cuando la lista está muy desbalanceada)
- No es estable (puede reordenar elementos iguales)

##  Ejemplo de entrada y salida

```python
Entrada: [33, 10, 55, 71, 29, 5, 12]
Salida:  [5, 10, 12, 29, 33, 55, 71]
