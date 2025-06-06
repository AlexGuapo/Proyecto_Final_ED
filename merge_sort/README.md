# Merge Sort

Merge Sort es un algoritmo de ordenamiento basado en la técnica de divide y vencerás. Divide la lista en mitades, ordena cada mitad recursivamente y luego las combina en una lista ordenada.

##  ¿Cómo funciona?

1. Divide la lista en dos mitades.
2. Ordena cada mitad recursivamente.
3. Combina ambas mitades en orden.

Este proceso se repite hasta que las sublistas contienen un solo elemento.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n log n)  |
| Promedio     | O(n log n)  |
| Peor caso    | O(n log n)  |

##  Ventajas

- Eficiente y estable
- Ideal para listas grandes
- Rendimiento constante sin importar el orden de entrada

##  Desventajas

- Uso adicional de memoria (por las listas auxiliares)
- Más complejo de implementar que otros métodos simples

##  Ejemplo de entrada y salida

```python
Entrada: [38, 27, 43, 3, 9, 82, 10]
Salida:  [3, 9, 10, 27, 38, 43, 82]
