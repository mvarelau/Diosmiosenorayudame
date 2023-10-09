#Es primo o no 
def es_primo(numero):
    i = 2
    while i*i <= numero:
        if numero % i == 0:
            return False
        i += 1
    return True

#imprimir los numeros 
def imprimir_numeros_primos():
    num = 1
    while num <= 100:
        if es_primo(num):
            print(num, end=" ")
        num += 1

print("Números primos del 1 al 100:")
imprimir_numeros_primos()
