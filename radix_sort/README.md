# Radix Sort

Radix Sort es un algoritmo de ordenamiento no comparativo que organiza los números procesando sus dígitos individualmente, desde el menos significativo hasta el más significativo. En cada paso, se agrupan los elementos por el valor del dígito correspondiente y se ordenan esos grupos usando **Bucket Sort**, tal como está implementado en este proyecto.

Esta versión del algoritmo reutiliza el módulo `bucket_sort`, lo que mejora la organización del código y la modularidad general.

##  ¿Cómo funciona?

1. Encuentra cuántos dígitos tiene el número más grande.
2. Para cada dígito (unidad, decena, centena...):
   - Agrupa los números en buckets según el valor de ese dígito.
   - Ordena cada bucket usando la función `ordenar_bucket()` del módulo `bucket_sort`.
   - Combina los buckets en una sola lista.
3. Repite hasta haber procesado todos los dígitos.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(nk)       |
| Promedio     | O(nk)       |
| Peor caso    | O(nk)       |

> `n`: número de elementos  
> `k`: cantidad de dígitos en el número más grande

##  Ventajas

- Muy eficiente para enteros con dígitos acotados
- Modular: usa el método `ordenar_bucket()` para ordenar internamente
- Estable (conserva el orden de elementos iguales)

##  Desventajas

- Solo funciona con números enteros no negativos (en esta implementación)
- Usa estructuras auxiliares (buckets), lo que implica mayor uso de memoria

##  Ejemplo de entrada y salida

```python
Entrada: [170, 45, 75, 90, 802, 24, 2, 66]
Salida:  [2, 24, 45, 66, 75, 90, 170, 802]
