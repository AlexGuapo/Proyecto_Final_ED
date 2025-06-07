# Bucket Sort

Bucket Sort es un algoritmo de ordenamiento no comparativo que distribuye los elementos en varios contenedores llamados "buckets". Luego, cada bucket se ordena individualmente utilizando un algoritmo auxiliar, en este caso, **Insertion Sort** (reutilizando la implementación del proyecto).

A diferencia de implementaciones básicas, esta versión de Bucket Sort **admite números en cualquier rango** (positivos, negativos, decimales o enteros).

##  ¿Cómo funciona?

1. Se calcula el rango de los datos y se distribuyen proporcionalmente en buckets.
2. Cada bucket se ordena usando la función `ordenar_insercion()` desde el módulo `insertion_sort`.
3. Los buckets se combinan para formar la lista final ordenada.

##  Complejidad

| Caso         | Complejidad |
|--------------|-------------|
| Mejor caso   | O(n + k)    |
| Promedio     | O(n + k)    |
| Peor caso    | O(n²)       |

> `n`: número de elementos  
> `k`: número de buckets

##  Ventajas

- Eficiente para listas con datos distribuidos uniformemente
- Modular: aprovecha el método de ordenamiento `ordenar_insercion()`
- Funciona con valores fuera del rango [0, 1]

##  Desventajas

- Requiere espacio adicional para los buckets
- El rendimiento depende de la distribución de los datos

##  Ejemplo de entrada y salida

```python
Entrada: [4.2, 3.1, 5.5, 2.7, 3.9, 1.0, 4.8]
Salida:  [1.0, 2.7, 3.1, 3.9, 4.2, 4.8, 5.5]
