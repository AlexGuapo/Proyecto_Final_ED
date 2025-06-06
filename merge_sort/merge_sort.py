def ordenar_merge(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        parte_izquierda = lista[:mitad]
        parte_derecha = lista[mitad:]

        # Ordena recursivamente ambas mitades
        ordenar_merge(parte_izquierda)
        ordenar_merge(parte_derecha)

        # Mezcla las mitades ordenadas
        i = j = k = 0

        while i < len(parte_izquierda) and j < len(parte_derecha):
            if parte_izquierda[i] < parte_derecha[j]:
                lista[k] = parte_izquierda[i]
                i += 1
            else:
                lista[k] = parte_derecha[j]
                j += 1
            k += 1

        # Copia los elementos restantes de cada mitad (si hay)
        while i < len(parte_izquierda):
            lista[k] = parte_izquierda[i]
            i += 1
            k += 1

        while j < len(parte_derecha):
            lista[k] = parte_derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", numeros)
    ordenar_merge(numeros)
    print("Lista ordenada:", numeros)
