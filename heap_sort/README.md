# Heap Sort

Heap Sort es un algoritmo de ordenamiento basado en la estructura de datos llamada heap (montículo). Construye un heap máximo y luego extrae el elemento más grande (la raíz) colocándolo al final, repitiendo el proceso para el resto de la lista.

##  ¿Cómo funciona?

1. Construye un heap máximo a partir de la lista.
2. Extrae el mayor elemento (la raíz) y lo coloca al final.
3. Restaura la propiedad de heap y repite hasta ordenar toda la lista.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n log n)  |
| Promedio     | O(n log n)  |
| Peor caso    | O(n log n)  |

##  Ventajas

- Complejidad garantizada O(n log n)
- No requiere recursión como Merge Sort
- No es sensible al orden inicial

##  Desventajas

- No es estable
- Más complejo que métodos simples como Bubble o Insertion

##  Ejemplo de entrada y salida

```python
Entrada: [12, 11, 13, 5, 6, 7]
Salida:  [5, 6, 7, 11, 12, 13]
