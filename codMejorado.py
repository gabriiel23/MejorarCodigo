import random
import time

# Genera una lista de números aleatorios
def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

# Encuentra el máximo elemento y a la vez los suma en una sola pasada
def maximo_y_suma(lista):
    maximo = lista[0]
    suma = 0
    for num in lista:
        if num > maximo:
            maximo = num
        suma += num
    return maximo, suma

# Main
if __name__ == "__main__":
    tamano_lista = 1000
    inicio_total = time.time()

    lista = generar_lista(tamano_lista)
    maximo, suma = maximo_y_suma(lista)

    fin_total = time.time()

    # Imprimir solo una parte de la lista para evitar una salida muy larga
    print(f"Lista (primeros 10 elementos): {lista[:10]} ... [Total elementos: {len(lista)}]")
    print(f"Máximo: {maximo}")
    print(f"Suma: {suma}")

    print(f"Tiempo total de ejecución: {fin_total - inicio_total:.6f} segundos")
