def ordenar_insercion(lista):
    for posicion_actual in range(1, len(lista)):
        elemento_actual = lista[posicion_actual]
        posicion_comparacion = posicion_actual - 1

        # Recorre la parte ordenada hacia la izquierda
        while posicion_comparacion >= 0 and lista[posicion_comparacion] > elemento_actual:
            lista[posicion_comparacion + 1] = lista[posicion_comparacion]
            posicion_comparacion -= 1

        lista[posicion_comparacion + 1] = elemento_actual

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [29, 10, 14, 37, 13]
    print("Lista original:", numeros)
    ordenar_insercion(numeros)
    print("Lista ordenada:", numeros)
