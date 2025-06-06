def ordenar_burbuja(lista):
    total_elementos = len(lista)

    for pasada in range(total_elementos):
        for indice in range(0, total_elementos - pasada - 1):
            elemento_actual = lista[indice]
            siguiente_elemento = lista[indice + 1]

            # Intercambia si están en el orden incorrecto
            if elemento_actual > siguiente_elemento:
                lista[indice], lista[indice + 1] = siguiente_elemento, elemento_actual

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", numeros)
    ordenar_burbuja(numeros)
    print("Lista ordenada:", numeros)
