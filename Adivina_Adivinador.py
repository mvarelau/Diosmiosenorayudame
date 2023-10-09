from random import*

def adivinar_numero():
    x=input("Ingrese un npumero del 1 al 100: ")
    min_numero = 1
    max_numero = 100
    bandera = False
    
    while not bandera:
        a = randint(min_numero, max_numero)
        respuesta = input(f"¿Es el número mayor, menor o igual que {a}?:  ")
        
        if respuesta == "mayor":
            min_numero = a 
        elif respuesta == "menor":
            max_numero = a 
        elif respuesta == "igual":
            print(f"Tu número es {a}")
            break 
            

adivinar_numero()
