import sys
import os

# Permitir importar desde bucket_sort
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bucket_sort')))
from bucket_sort import ordenar_bucket

def contar_max_digitos(lista):
    #Devuelve el número máximo de dígitos en los números de la lista.
    if not lista:
        return 0
    return len(str(max(lista)))

def ordenar_radix(lista):
    #Ordena una lista de enteros no negativos usando Radix Sort,delegando el ordenamiento interno de los buckets a Bucket Sort.
    max_digitos = contar_max_digitos(lista)
    posicion = 1  # dígito menos significativo

    for _ in range(max_digitos):
        # Crear 10 buckets para dígitos del 0 al 9
        buckets = [[] for _ in range(10)]

        for numero in lista:
            digito = (numero // posicion) % 10
            buckets[digito].append(numero)

        # Ordenar cada bucket usando bucket_sort
        for bucket in buckets:
            ordenar_bucket(bucket)

        # Reconstruir lista original
        lista.clear()
        for bucket in buckets:
            lista.extend(bucket)

        posicion *= 10

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", numeros)
    ordenar_radix(numeros)
    print("Lista ordenada:", numeros)
