def ordenar_quick(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [elemento for elemento in lista[1:] if elemento <= pivote]
        mayores = [elemento for elemento in lista[1:] if elemento > pivote]
        return ordenar_quick(menores) + [pivote] + ordenar_quick(mayores)

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [33, 10, 55, 71, 29, 5, 12]
    print("Lista original:", numeros)
    lista_ordenada = ordenar_quick(numeros)
    print("Lista ordenada:", lista_ordenada)
