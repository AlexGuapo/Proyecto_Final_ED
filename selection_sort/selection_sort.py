def ordenar_seleccion(lista):
    total_elementos = len(lista)

    for posicion_actual in range(total_elementos):
        indice_minimo = posicion_actual

        # Busca el valor mínimo en la parte no ordenada
        for indice in range(posicion_actual + 1, total_elementos):
            if lista[indice] < lista[indice_minimo]:
                indice_minimo = indice

        # Intercambia el mínimo encontrado con el primer elemento no ordenado
        if indice_minimo != posicion_actual:
            lista[posicion_actual], lista[indice_minimo] = lista[indice_minimo], lista[posicion_actual]

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [64, 25, 12, 22, 11]
    print("Lista original:", numeros)
    ordenar_seleccion(numeros)
    print("Lista ordenada:", numeros)
