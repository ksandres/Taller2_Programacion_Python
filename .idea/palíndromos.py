def es_palindromo(numero):

    numero_str = str(numero)

    #
    if numero_str == numero_str[::-1]:
        return True
    else:
        return False



numero = input("Ingrese un numero: ")
numero= int(numero_str)
if es_palindromo(numero):
    print(numero, "es palindromo")
else:
    print(numero, "no es palindromo")