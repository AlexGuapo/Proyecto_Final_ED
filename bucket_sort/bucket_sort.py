import sys
import os

# Agrega la ruta de insertion_sort para importar su método
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'insertion_sort')))
from insertion_sort import ordenar_insercion

def ordenar_bucket(lista):
    #Ordena una lista de números (enteros o decimales) usando Bucket Sort,reutilizando el algoritmo Insertion Sort para cada bucket.
    if not lista:
        return

    valor_minimo = min(lista)
    valor_maximo = max(lista)
    rango = valor_maximo - valor_minimo

    if rango == 0:
        return  # Todos los elementos son iguales

    cantidad_buckets = len(lista)
    buckets = [[] for _ in range(cantidad_buckets)]

    # Distribuir los elementos en buckets
    for numero in lista:
        indice_bucket = int(((numero - valor_minimo) / rango) * (cantidad_buckets - 1))
        buckets[indice_bucket].append(numero)

    # Ordenar cada bucket usando tu método de inserción
    for bucket in buckets:
        ordenar_insercion(bucket)

    # Reconstruir la lista ordenada
    lista.clear()
    for bucket in buckets:
        lista.extend(bucket)

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [4.2, 3.1, 5.5, 2.7, 3.9, 1.0, 4.8]
    print("Lista original:", numeros)
    ordenar_bucket(numeros)
    print("Lista ordenada:", numeros)