n = int(input("¿Cuántos valores ingresará? "))


datos = []


for i in range(1, n + 1):
    valor = float(input(f"Valor {i}: "))
    datos.append(valor)


rango = max(datos) - min(datos)


print(f"El rango es {rango:.2f}")