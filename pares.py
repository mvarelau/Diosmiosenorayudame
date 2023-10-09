def imprimir_pares_descendentes(n):
    if n < 2:
        print("El número debe ser mayor o igual a 2.")
        return
    num = n if n % 2 == 0 else n - 1  
    while num >= 2:
        print(num)
        num -= 2


n = int(input("Ingrese un número natural (n ≥ 2): "))
print("Números pares descendentes hasta 2:")
imprimir_pares_descendentes(n)
