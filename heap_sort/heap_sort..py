def heapify(lista, tamaño_heap, raiz):
    #Asegura que el subárbol con raíz en `raiz` mantenga la propiedad de heap máximo.
    mayor = raiz
    hijo_izquierdo = 2 * raiz + 1
    hijo_derecho = 2 * raiz + 2

    # Verifica si el hijo izquierdo es mayor que la raíz
    if hijo_izquierdo < tamaño_heap and lista[hijo_izquierdo] > lista[mayor]:
        mayor = hijo_izquierdo

    # Verifica si el hijo derecho es mayor que el valor actual más grande
    if hijo_derecho < tamaño_heap and lista[hijo_derecho] > lista[mayor]:
        mayor = hijo_derecho

    # Si el mayor no es la raíz, intercambia y aplica heapify recursivamente
    if mayor != raiz:
        lista[raiz], lista[mayor] = lista[mayor], lista[raiz]
        heapify(lista, tamaño_heap, mayor)

def ordenar_heap(lista):
    tamaño_lista = len(lista)

    # Construye el heap máximo
    for i in range(tamaño_lista // 2 - 1, -1, -1):
        heapify(lista, tamaño_lista, i)

    # Extrae los elementos del heap uno por uno
    for i in range(tamaño_lista - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]  # mueve el mayor al final
        heapify(lista, i, 0)

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [12, 11, 13, 5, 6, 7]
    print("Lista original:", numeros)
    ordenar_heap(numeros)
    print("Lista ordenada:", numeros)
