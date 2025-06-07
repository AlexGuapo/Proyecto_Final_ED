def contar_max_digitos(lista):
    #Devuelve el número máximo de dígitos en los números de la lista.
    if not lista:
        return 0
    return len(str(max(lista)))

def ordenar_radix(lista):
    max_digitos = contar_max_digitos(lista)
    posicion = 1  # empezamos desde el dígito menos significativo

    for _ in range(max_digitos):
        # Crea 10 "buckets" para cada dígito (0 al 9)
        buckets = [[] for _ in range(10)]

        for numero in lista:
            digito = (numero // posicion) % 10
            buckets[digito].append(numero)

        # Reconstruye la lista uniendo los buckets
        lista.clear()
        for bucket in buckets:
            lista.extend(bucket)

        posicion *= 10  # pasa al siguiente dígito

# Ejemplo de uso
if __name__ == "__main__":
    numeros = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", numeros)
    ordenar_radix(numeros)
    print("Lista ordenada:", numeros)
